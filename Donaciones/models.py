from django.db import models
from django.urls import reverse


# Create your models here.

class ArchivoCarga(models.Model):
    """Model definition for ArchivoCarga."""
    archivo = models.FileField(("Archivo"), upload_to="static/cargas/", max_length=200)
    fecha = models.DateTimeField(("Fecha de carga"), auto_now=False, auto_now_add=True)

    class Meta:

        verbose_name = 'Archivo de Carga'
        verbose_name_plural = 'Archivos de Carga'

    def __str__(self):
        return self.archivo.name


class Donante(models.Model):
    
    tipo_persona = models.CharField(("Tipo de Persona"), max_length=50, blank=True, null=True)
    nombre = models.CharField(("Nombre"), max_length=300,blank=True, null=True)
    primer_nombre = models.CharField(("Primer Nombre"), max_length=100, blank=True, null=True)
    segundo_nombre = models.CharField(("Segundo Nombre"), max_length=100, blank=True, null=True)
    primer_apellido = models.CharField(("Primer Apellido"), max_length=100, blank=True, null=True)
    segundo_apellido = models.CharField(("Segundo Apellido"), max_length=100, blank=True, null=True)


    # TODO: Define fields here

    class Meta:
        """Meta definition for Donante."""

        verbose_name = 'Donante'
        verbose_name_plural = 'Donantes'

    def __str__(self):
        """Unicode representation of Donante."""
        if self.nombre:
            return f'{self.nombre}'
        else:
            return f'{self.primer_nombre} {self.segundo_nombre} {self.primer_apellido} {self.segundo_apellido}'

    def get_absolute_url(self):
            return reverse("donante_detail", kwargs={"pk": self.pk})


class Partido(models.Model):

    nombre = models.CharField(("Nombre"), max_length=200,blank=True, null=True)
    siglas = models.CharField(("Siglas"), max_length=50,blank=True, null=True)

    class Meta:
        verbose_name = ("partido")
        verbose_name_plural = ("partidos")

    def __str__(self):
        return self.siglas

    def get_absolute_url(self):
        return reverse("partido_detail", kwargs={"pk": self.pk})


class Donacion(models.Model):
    monto = models.DecimalField(("Monto"), max_digits=10, decimal_places=2,blank=True, null=True)
    donante = models.ForeignKey('Donaciones.Donante', on_delete=models.CASCADE,blank=True, null=True,editable= False)
    partido = models.ForeignKey('Donaciones.Partido', on_delete=models.CASCADE,blank=True, null=True)
    ano = models.IntegerField(("Año"),blank=True, null=True)
    financiamiento = models.CharField(("Financiamiento"), max_length=50,blank=True, null=True)
    carga = models.ForeignKey("Donaciones.ArchivoCarga", verbose_name=("Id_Carga"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("donacion")
        verbose_name_plural = ("donaciones")

    def __str__(self):
        return f"{self.donante} - {self.monto} - {self.partido}"

    def get_absolute_url(self):
        return reverse("donacion_detail", kwargs={"pk": self.pk})


class ListaNombres(models.Model):
    nombre_pila = models.CharField(("Nombre de Pila"), max_length=100)

    class Meta:

        verbose_name = 'Lista de Nombres'
        verbose_name_plural = 'ListaNombress'

    def __str__(self):
        return f'{self.nombre_pila}'
    

class ListaApellidos(models.Model):
    apellido = models.CharField(("Apellido"), max_length=100)
    class Meta:
        verbose_name = 'Lista de Apellidos'
        verbose_name_plural = 'ListaApellidoss'

    def __str__(self):
        return f'{self.apellido}' # TODO

