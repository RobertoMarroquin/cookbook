from django.contrib import admin
from .models import Donacion,Donante,Partido

class DonanteAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(Donante, DonanteAdmin)

class PartidoAdmin(admin.ModelAdmin):
    list_display = ('siglas',)

admin.site.register(Partido, PartidoAdmin)

class DonacionAdmin(admin.ModelAdmin):
    list_display = ('donante','partido','monto','ano','financiamiento')
    list_filter = ('partido','ano')
    search_fields = ('donante__nombre',)

admin.site.register(Donacion, DonacionAdmin)
