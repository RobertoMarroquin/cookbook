from django.urls import path

from .views import DonanteListView,PartidoListView

app_name = 'donaciones'

urlpatterns = [
    path('donantes/', DonanteListView.as_view(), name='donantes'),
    path("partidos/", PartidoListView.as_view(), name="partidos")

]

