# core/views.py
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

class RelatorioView(View):
    def get(self, request):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="relatorio.pdf"'

        p = canvas.Canvas(response, pagesize=A4)
        p.drawString(100, 800, "Relatório de Abastecimentos")

        # Adicione lógica para coletar dados e gerar o PDF

        p.showPage()
        p.save()
        return response
