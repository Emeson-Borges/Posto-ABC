from django.db import models

class Tanque(models.Model):
    TIPO_COMBUSTIVEL = [
        ('GASOLINA', 'Gasolina'),
        ('DIESEL', 'Óleo Diesel'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_COMBUSTIVEL)

    def __str__(self):
        return f"{self.tipo} - Tanque {self.id}"

class Bomba(models.Model):
    tanque = models.ForeignKey(Tanque, on_delete=models.CASCADE)

    def __str__(self):
        return f"Bomba {self.id} - {self.tanque}"

class Abastecimento(models.Model):
    bomba = models.ForeignKey(Bomba, on_delete=models.CASCADE)
    quantidade_litros = models.FloatField()
    valor_abastecido = models.DecimalField(max_digits=10, decimal_places=2)
    imposto = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.imposto = self.valor_abastecido * 0.13
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.data} - Bomba {self.bomba.id}"
