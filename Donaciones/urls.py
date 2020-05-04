from django.urls import path

from .views import DonanteListView,PartidoListView,EmpresaListView,CargaView,ArchivoCargaDeleteView

app_name = 'donaciones'

urlpatterns = [
    path('carga/', CargaView.as_view(), name='carga'),
    path('donantes/', DonanteListView.as_view(), name='donantes'),
    path('juridicos/', EmpresaListView.as_view(), name='juridicos'),
    path("partidos/", PartidoListView.as_view(), name="partidos"),
    path("eliminar/<int:pk>/", ArchivoCargaDeleteView.as_view(), name="eliminar")

]

