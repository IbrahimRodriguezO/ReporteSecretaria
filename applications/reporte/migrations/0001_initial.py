# Generated by Django 5.1.5 on 2025-01-16 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField(verbose_name='Día')),
                ('hora', models.TimeField(verbose_name='Hora')),
                ('tema', models.CharField(max_length=200, verbose_name='Tema')),
                ('integrantes', models.TextField(verbose_name='Integrantes')),
                ('lugar', models.CharField(max_length=200, verbose_name='Lugar')),
            ],
            options={
                'verbose_name': 'Reporte',
                'verbose_name_plural': 'Reportes',
                'db_table': 'reporte',
            },
        ),
    ]