# Generated by Django 5.0.6 on 2024-06-21 14:50

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tanque',
            name='tipo',
        ),
        migrations.AddField(
            model_name='bomba',
            name='numero',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tanque',
            name='data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='tanque',
            name='nome',
            field=models.CharField(default=2024, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tanque',
            name='tipo_combustivel',
            field=models.CharField(choices=[('GASOLINA', 'Gasolina'), ('DIESEL', 'Óleo Diesel')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='abastecimento',
            name='bomba',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abastecimentos', to='core.bomba'),
        ),
        migrations.AlterField(
            model_name='abastecimento',
            name='data',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='abastecimento',
            name='quantidade_litros',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='bomba',
            name='tanque',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bombas', to='core.tanque'),
        ),
    ]
