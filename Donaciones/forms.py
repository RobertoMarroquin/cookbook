from django import forms


class CargaForm(forms.Form):
    archivo = forms.FileField()