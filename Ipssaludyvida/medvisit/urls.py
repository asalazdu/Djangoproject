from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='inicio'),
    path('crearPaciente', views.crearPaciente, name='crearPaciente'),
    path('crearAtencion', views.crearAtencion, name='crearAtencion'),
    path('listarPacientes', views.listarPacientes, name='listarPacientes'),
    path('listarAtenciones', views.listarAtenciones, name='listarAtenciones'),
    path('editarPaciente/<id>', views.editarPaciente, name='editarPaciente'),
    path('editarAtencion/<id>', views.editarAtencion, name='editarAtencion'),
    path('eliminarPaciente/<id>', views.eliminarPaciente),
    path('eliminarAtencion/<id>', views.eliminarAtencion),
    path('detallePaciente/<id>', views.detallePaciente),
    path('detalleAtencion/<id>', views.detalleAtencion)
]