from django.test import TestCase, Client
from django.urls import reverse
from .models import Tanque, Bomba, Abastecimento
import datetime

class AbastecimentoModelTest(TestCase):
    def setUp(self):
        tanque = Tanque.objects.create(nome='Tanque de Gasolina', tipo_combustivel='Gasolina')
        bomba = Bomba.objects.create(tanque=tanque, numero=1)
        self.abastecimento = Abastecimento.objects.create(
            bomba=bomba,
            data=datetime.date.today(),
            quantidade_litros=50,
            valor_abastecido=200,
        )

    def test_imposto_calculado_corretamente(self):
        imposto_esperado = 200 * 0.13
        self.assertEqual(self.abastecimento.imposto, imposto_esperado)

class RelatorioAbastecimentosTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_relatorio_abastecimentos_status_code(self):
        url = reverse('relatorio_abastecimentos')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

  