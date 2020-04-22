from django.shortcuts import render
from django.views.generic import DeleteView,ListView,CreateView,DeleteView,View
from django.db.models import Sum


import csv
import os


from .models import Donante,Donacion,Partido,ListaApellidos,ListaNombres

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def carga():
   with open(os.path.join(BASE_DIR,"Union2 - Base-naturales.csv")) as f:
        documento = csv.reader(f,delimiter=',',dialect='excel')
        next(documento, None)
        documento = list(documento)
        lista_nombres = list(ListaNombres.objects.all())
        lista_apellidos = list(ListaApellidos.objects.all())
        listaA = []
        listaN = []
        for apellido in lista_apellidos:
            listaA.append(apellido.apellido)
        
        for nombre in lista_nombres:
            listaN.append(nombre.nombre_pila)
        
        for linea in documento:
            nombre,monto,ano,siglas,financiamiento,tipo_persona = list(linea)
            n1,a1 = False, False
            if tipo_persona in ("NATURAL","NATURALES"):
                tipo_persona = "NATURAL"
                n1,n2,a1,a2 = compara_antroponimos(nombre,listaN,listaA) if   compara_antroponimos(nombre,listaN,listaA) != "No se pudo Ordenar" else (False,False,False,False)  
            if tipo_persona in ("JURIDICA", "JURÍDICA", "JURÍDICO", "JURIDICO"):
                tipo_persona = "JURIDICA"
            if tipo_persona in ("INDETERMINADO","INDETERMINADA"):
                tipo_persona = "INDETERMINADO"
            monto = float(monto)
            ano = int(ano)
            
            if n1 and a1:
                nombre_compuesto = f'{n1} {n2} {a1} {a2}'.strip().replace("  "," ")          
                donante = Donante.objects.get_or_create(
                nombre =nombre_compuesto,
                primer_nombre = n1,
                segundo_nombre = n2,
                primer_apellido = a1,
                segundo_apellido = a2,
                tipo_persona = tipo_persona,
                )
            else:
                donante = Donante.objects.get_or_create(
                    nombre = nombre,
                    tipo_persona = tipo_persona,
                )


            partido = Partido.objects.get_or_create(
               siglas = siglas,
            )

            donacion = Donacion.objects.create(
               donante = donante[0],
               partido = partido[0],
               monto = float(monto),
               ano = int(ano),
               financiamiento  = financiamiento,
            )

def carga_nombres():
    with open(os.path.join(BASE_DIR,"nombres.csv")) as f:
        documento = csv.reader(f,delimiter=',',dialect='excel')
        documento = list(documento)
        for linea in documento:
            nombre = linea[0]
            registro  = ListaNombres.objects.get_or_create(nombre_pila=nombre)


def carga_apellidos():
    with open(os.path.join(BASE_DIR,"apellidos.csv")) as f:
        documento = csv.reader(f,delimiter=',',dialect='excel')
        documento = list(documento)
        for linea in documento:
            apellido = linea[0]
            registro  = ListaApellidos.objects.get_or_create(apellido=apellido)


class DonanteListView(ListView):
    model = Donante
    template_name = "Donaciones/lista_donantes.html"
    context_object_name = 'donantes'
    
    def get_context_data(self, **kwargs):
        context = super(DonanteListView, self).get_context_data(**kwargs)
        context['donantes'] = Donante.objects.order_by('-id')[:10][::-1]
        nombres = self.request.GET.get('nombres')
        apellidos = self.request.GET.get('apellidos')
        context['tipo']='Natural'
        if nombres and nombres != "" and apellidos and apellidos != '':
            context['donantes'] = Donante.objects.filter(nombre__icontains=nombres).filter(nombre__icontains=apellidos).filter(tipo_persona='NATURAL')
            context['donaciones'] = Donacion.objects.filter(donante_id__in=(context['donantes']))
        else:
            context['error'] = "Falta Informacion"

        return context


class EmpresaListView(ListView):
    model = Donante
    template_name = "Donaciones/lista_donantes.html"
    context_object_name = 'donantes'
    
    def get_context_data(self, **kwargs):
        context = super(EmpresaListView, self).get_context_data(**kwargs)
        context['donantes'] = Donante.objects.filter(tipo_persona="JURIDICA").order_by('-id')[:10][::-1]
        nombre = self.request.GET.get('nombre')
        context['tipo']='Juridica'
        if nombre and nombre != "":
            context['donantes'] = Donante.objects.filter(nombre__icontains=nombre).filter(tipo_persona='JURIDICA')
            context['donaciones'] = Donacion.objects.filter(donante_id__in=(context['donantes']))
        else:
            context['error'] = "Falta Informacion"

        return context
    
    


class PartidoListView(ListView):
    model = Partido
    template_name = "Donaciones/lista_partido.html"
    context_object_name = 'partidos'

    
    def get_context_data(self, **kwargs):
        context = super(PartidoListView, self).get_context_data(**kwargs)
        context["donaciones"] = Donacion.objects.all().values("partido","ano").annotate(monto_anual=Sum("monto"))
        return context
    

    def get_queryset(self):
        nombre = self.request.GET.get('nombre')
        last_ten = Partido.objects.all().order_by('-id')

        if nombre:
            donantes = Partido.objects.filter(siglas__icontains=nombre)
            return donantes
        return last_ten



def compara_antroponimos(nombre,listaNombres,listaApellidos):

    nombre = " " + nombre.upper()

    nombre = nombre.replace("  "," ")
    nombre = nombre.replace(" DE "," DE_")
    nombre = nombre.replace(" LA "," LA_") 
    nombre = nombre.replace(" DEL "," DEL_")
    nombre = nombre.replace(",","")
    nombre = nombre.strip()

    nombres = list(nombre.split())
    largo = len(nombres)
    a1 = ""
    a2 = ""
    n1 = ""
    n2 = ""        

    if largo == 4 :
        if nombres[0] in listaNombres and nombres[1] in listaNombres and nombres[2] in listaApellidos and nombres[3] in listaApellidos:
            n1,n2,a1,a2 = nombres
        elif nombres[0] in listaApellidos and nombres[1] in listaApellidos  and nombres[2] in listaNombres and nombres[3] in listaNombres:
            a1,a2,n1,n2 = nombres
        else:
            return "No se pudo Ordenar"

    elif largo == 3:
        if nombres[0] in listaApellidos and nombres[1] in listaApellidos and nombres[2] in listaNombres:
            a1,a2,n1 = nombres
        elif nombres[0] in listaApellidos and nombres[1] in listaNombres and nombres[2] in listaNombres:
            a1,n1,n2 = nombres
        elif nombres[0] in listaNombres and nombres[1] in listaApellidos and nombres[2] in listaApellidos:
            n1,a1,a2 = nombres
        elif nombres[0] in listaNombres and nombres[1] in listaNombres and nombres[2] in listaApellidos:
            n1,n2,a1 = nombres
        else:
            return "No se pudo Ordenar"

    elif largo == 2:
        if nombres[0] in listaNombres and nombres[1] in listaApellidos:
            n1,a1 = nombres
        elif nombres[0] in listaApellidos and nombres[1] in listaNombres:
            a1,n1 = nombres
        else:
            return "No se pudo Ordenar"

    else:
        return "No se pudo Ordenar"

    tupla = (n1,n2,a1,a2)
    return  tupla


class CargaView(View):
    def get(self, request, *args, **kwargs):

        return render(request,"Donaciones/carga.html",context={})

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')    


def reemplazo_espacios():
    listaN = ListaNombres.objects.filter(nombre_pila__icontains="de ") | ListaNombres.objects.filter(nombre_pila__icontains="del ") | ListaNombres.objects.filter(nombre_pila__icontains="la ")
    listaA = ListaApellidos.objects.filter(apellido__icontains="de ") | ListaApellidos.objects.filter(apellido__icontains="del ") | ListaApellidos.objects.filter(apellido__icontains="la ")

    for n in listaN:
        n.nombre_pila = n.nombre_pila.replace("  "," ")
        n.nombre_pila = n.nombre_pila.replace("DE ","DE_")
        n.nombre_pila = n.nombre_pila.replace("DE ","DE_")
        n.nombre_pila = n.nombre_pila.replace("DE ","DE_")
        n.save()

    for a in listaA:
        a.apellido = a.apellido.replace("  "," ") 
        a.apellido = a.apellido.replace("DE ","DE_") 
        a.apellido = a.apellido.replace("DEL ","DEL_") 
        a.apellido = a.apellido.replace("LA ","LA_") 
        a.save()



    