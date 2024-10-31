from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

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
    path('login/', views.login_view, name='login'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="public/login/auth_forgot_password.html"), name='password_reset'),

    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(template_name="public/login/auth_password_reset_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="public/login/password-confirm.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="public/login/password_reset_complete.html"), name='password_reset_complete'),
]