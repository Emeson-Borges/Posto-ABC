from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic.base import View
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from rest_framework import viewsets


from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Paragraph
from rest_framework import viewsets

from .models import Abastecimento, Bomba, Tanque
from .serializers import AbastecimentoSerializer, BombaSerializer, TanqueSerializer


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
    # Configuração inicial do PDF
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = (
        'attachment; filename="relatorio_abastecimentos.pdf"'
    )

    # Criar um objeto canvas.Canvas para escrever o PDF final
    p = canvas.Canvas(response, pagesize=A4)

    
    # Título do relatório
    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, 800, "Relatório de Abastecimentos")
    p.drawString(50, 900, "Teste")

    # Recuperar todos os abastecimentos
    abastecimentos = Abastecimento.objects.all()

    # Posição inicial para escrever os dados
    y = 750
    for abastecimento in abastecimentos:
        p.setFont("Helvetica", 12)
        p.drawString(50, y, f"Data: {abastecimento.data.strftime('%d/%m/%Y')}")
        p.drawString(250, y, f"Tanque: {abastecimento.bomba.tanque.tipo_combustivel}")
        p.drawString(450, y, f"Bomba: {abastecimento.bomba.bomba_utilizada}")
        p.drawString(600, y, f"Valor: R$ {abastecimento.valor_abastecido:.2f}")
        y -= 20

    # Calcular e exibir a soma total do período
    total = (
        abastecimentos.aggregate(total_periodo=Sum("valor_abastecido"))["total_periodo"]
        or 0
    )
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, y - 40, f"Soma Total do Período: R$ {total:.2f}")

    # Finaliza o PDF
    p.showPage()
    p.save()

    # Retornar o response com o PDF gerado
    return response
