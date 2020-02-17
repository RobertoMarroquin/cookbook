from django.shortcuts import render
from django.views.generic import DeleteView,ListView,CreateView,DeleteView


import csv
import os


from .models import Donante,Donacion,Partido

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#def carga(archivo):
#    with open(os.path.join(BASE_DIR,archivo)) as f:
#        documento = csv.reader(f,delimiter=',',dialect='excel')
#        next(documento, None)
#        documento = list(documento)
#        for linea in documento:
#
#            nombre,monto,ano,siglas,financiamiento,tipo_persona = list(linea)
#            monto = float(monto)
#            ano = int(ano)
#            print(list(linea))
#
#            donante = Donante.objects.get_or_create(
#                nombre = nombre,
#                tipo_persona = tipo_persona,
#            )
#
#            partido = Partido.objects.get_or_create(
#                siglas = siglas,
#            )
#
#            donacion = Donacion.objects.create(
#                donante = donante[0],
#                partido = partido[0],
#                monto = float(monto),
#                ano = int(ano),
#                financiamiento  = financiamiento,
#            )



class DonanteListView(ListView):
    model = Donante
    template_name = "Donaciones/lista_donantes.html"
    context_object_name = 'donantes'
    
    def get_context_data(self, **kwargs):
        context = super(DonanteListView, self).get_context_data(**kwargs)
        context['donantes'] = Donante.objects.order_by('-id')[:10][::-1]
        nombre = self.request.GET.get('nombre')

        if nombre and nombre != "":
            context['donantes'] = Donante.objects.filter(nombre__icontains=nombre)
            context['donaciones'] = Donacion.objects.filter(donante_id__in=(context['donantes']))
            
        return context
    
    


class PartidoListView(ListView):
    model = Partido
    template_name = "Donaciones/lista_partido.html"
    context_object_name = 'partidos'

    def get_queryset(self):
        nombre = self.request.GET.get('nombre')
        last_ten = Partido.objects.order_by('-id')[:10][::-1]

        if nombre:
            donantes = Partido.objects.filter(siglas__icontains=nombre)
            return donantes
        return last_ten

