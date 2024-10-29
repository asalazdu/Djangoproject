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
    path('eliminarPaciente/<id>', views.eliminarPaciente, name='eliminarPaciente'),
    path('eliminarAtencion/<id>', views.eliminarAtencion,  name='eliminarAtencion'),
    path('detallePaciente/<id>', views.detallePaciente, name='detallePaciente'),
    path('detalleAtencion/<id>', views.detalleAtencion,  name='detalleAtencion'),
    path('logout/', views.viewLogout,  name='logout'),
    path('register/', views.register,  name='register'),
]