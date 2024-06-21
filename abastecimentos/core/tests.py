# core/tests.py
from django.test import TestCase
from .models import Tanque, Bomba, Abastecimento

class TanqueTestCase(TestCase):
    def setUp(self):
        Tanque.objects.create(tipo="GASOLINA")

    def test_tanque_creation(self):
        tanque = Tanque.objects.get(tipo="GASOLINA")
        self.assertEqual(tanque.tipo, "GASOLINA")
