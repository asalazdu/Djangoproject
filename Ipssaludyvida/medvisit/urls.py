from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='inicio'),
    path('crearPaciente', views.crearPaciente, name='crearPaciente'),
    path('listarPacientes', views.listarPacientes, name='listarPacientes'),
    path('editarPaciente/<id>', views.editarPaciente, name='editarPaciente'),
    path('eliminarPaciente/<id>', views.eliminarPaciente),
    path('detallePaciente/<id>', views.detallePaciente)
]