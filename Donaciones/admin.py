from django.contrib import admin
from .models import Donacion,Donante,Partido,ListaNombres,ListaApellidos

class DonanteAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)

    list_display = ('nombre','primer_nombre','segundo_nombre','primer_apellido','segundo_apellido')

admin.site.register(Donante, DonanteAdmin)


class PartidoAdmin(admin.ModelAdmin):
    list_display = ('siglas',)

admin.site.register(Partido, PartidoAdmin)


class DonacionAdmin(admin.ModelAdmin):
    list_display = ('donante','partido','monto','ano','financiamiento')
    list_filter = ('partido','ano')
    search_fields = ('donante__nombre',)

admin.site.register(Donacion, DonacionAdmin)


class ListaNombresAdmin(admin.ModelAdmin):
    list_display = ('nombre_pila',)
    search_fields = ('nombre_pila',)


admin.site.register(ListaNombres, ListaNombresAdmin)


class ListaApellidosAdmin(admin.ModelAdmin):
    list_display = ('apellido',)
    search_fields = ('apellido',)

admin.site.register(ListaApellidos, ListaApellidosAdmin)
