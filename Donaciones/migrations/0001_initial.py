# Generated by Django 2.2.6 on 2020-02-04 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_persona', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tipo de Persona')),
                ('nombre', models.CharField(blank=True, max_length=300, null=True, verbose_name='Nombre')),
                ('nombres', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombres')),
                ('apellidos', models.CharField(blank=True, max_length=100, null=True, verbose_name='Apellidos')),
            ],
            options={
                'verbose_name': 'Donante',
                'verbose_name_plural': 'Donantes',
            },
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre')),
                ('siglas', models.CharField(blank=True, max_length=50, null=True, verbose_name='Siglas')),
            ],
            options={
                'verbose_name': 'partido',
                'verbose_name_plural': 'partidos',
            },
        ),
        migrations.CreateModel(
            name='Donacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Monto')),
                ('financiamiento', models.CharField(blank=True, max_length=50, null=True, verbose_name='Financiamiento')),
                ('ano', models.IntegerField(blank=True, null=True, verbose_name='Año')),
                ('donante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Donaciones.Donante')),
                ('partido', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Donaciones.Partido')),
            ],
            options={
                'verbose_name': 'donacion',
                'verbose_name_plural': 'donaciones',
            },
        ),
    ]
