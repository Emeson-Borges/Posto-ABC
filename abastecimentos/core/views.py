import os
from django.db.models import Sum
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from rest_framework import viewsets
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Image, PageTemplate, Frame
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from io import BytesIO
from pathlib import Path
from reportlab.lib.enums import TA_CENTER

from reportlab.lib.units import inch
from reportlab.lib import colors

from .models import Abastecimento, Bomba, Tanque
from .serializers import AbastecimentoSerializer, BombaSerializer, TanqueSerializer

base_dir = Path(__file__).resolve().parent.parent
logo_path = base_dir / 'core' / 'static' / 'images' / 'logo.png'

class TanqueViewSet(viewsets.ModelViewSet):
    queryset = Tanque.objects.all()
    serializer_class = TanqueSerializer


class BombaViewSet(viewsets.ModelViewSet):
    queryset = Bomba.objects.all()
    serializer_class = BombaSerializer


class AbastecimentoViewSet(viewsets.ModelViewSet):
    queryset = Abastecimento.objects.all()
    serializer_class = AbastecimentoSerializer


def relatorio_abastecimentos(request):
    # Recuperar todos os abastecimentos
    abastecimentos = Abastecimento.objects.all()

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    
    subtitle_style = ParagraphStyle(
    'Subtitle',
    parent=styles['Heading2'],
    fontSize=14,
    textColor='blue',
    alignment=TA_CENTER,
    spaceAfter=12
)
    body_style = styles["Normal"]

    elements = []

    # Função para criar cabeçalho
    def header(canvas, doc):
        canvas.saveState()
        canvas.drawImage(str(logo_path), A4[0] - inch - 50, A4[1] - inch - 50, width=1.5*inch, height=1*inch)
        canvas.setFont('Helvetica-Bold', 16)
        canvas.restoreState()

    # Definir o cabeçalho para todas as páginas
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height - inch, id='normal')
    template = PageTemplate(id='header', frames=frame, onPage=header)
    doc.addPageTemplates([template])

    # Título do relatório
    elements.append(Paragraph("Relatório de Abastecimentos", title_style))
    elements.append(Paragraph("Posto ABC", subtitle_style))
    elements.append(Paragraph("<br/><br/>", body_style))  
    
    # Tabela de abastecimentos
    data = []
    table_header = ["Data", "Tanque", "Bomba", "Valor"]
    data.append(table_header)

    for abastecimento in abastecimentos:
        row = [
            abastecimento.data.strftime('%d/%m/%Y'),
            abastecimento.bomba.tanque.tipo_combustivel,
            abastecimento.bomba.bomba_utilizada,
            f"R$ {abastecimento.valor_abastecido:.2f}"
        ]
        data.append(row)

    # Configuração da tabela
    table = Table(data, colWidths=[2*inch, 2*inch, 2*inch, 2*inch])
    table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black), 
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey), 
        ('ALIGN', (0, 0), (-1, -1), 'CENTER')  
    ]))
    elements.append(table)

    # Calcular e exibir a soma total do período
    total = abastecimentos.aggregate(total_periodo=Sum("valor_abastecido"))["total_periodo"] or 0
    total_text = f"<br/><br/><b>Soma Total do Período: R$ {total:.2f}</b>"
    elements.append(Paragraph(total_text, body_style))

    doc.build(elements)

    # Retornar o response com o PDF gerado
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatorio_abastecimentos.pdf"'
    response.write(buffer.getvalue())
    buffer.close()
    return response