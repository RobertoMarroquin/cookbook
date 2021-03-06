# Generated by Django 2.2.6 on 2020-02-24 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donaciones', '0002_auto_20200212_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListaApellidos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=100, verbose_name='apellido')),
            ],
            options={
                'verbose_name': 'ListaApellidos',
                'verbose_name_plural': 'ListaApellidoss',
            },
        ),
        migrations.CreateModel(
            name='ListaNombres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_pila', models.CharField(max_length=100, verbose_name='Nombre de Pila')),
            ],
            options={
                'verbose_name': 'ListaNombres',
                'verbose_name_plural': 'ListaNombress',
            },
        ),
    ]
