from django.urls import path

from .views import DonanteListView,PartidoListView,EmpresaListView

app_name = 'donaciones'

urlpatterns = [
    path('donantes/', DonanteListView.as_view(), name='donantes'),
    path('juridicos/', EmpresaListView.as_view(), name='juridicos'),
    path("partidos/", PartidoListView.as_view(), name="partidos"),

]

