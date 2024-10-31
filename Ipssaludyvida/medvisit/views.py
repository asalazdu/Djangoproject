from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from .forms import PacienteForm, ServicioSaludForm, CustomUserCreationForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm





@login_required
def home(request):
    pacientes = Paciente.objects.all()
    contexto = {
            'pacientes': pacientes,
        }
    
    return render(request, "public/pacientes/lista_pacientes.html", contexto)


def viewLogout(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(
                username=user_creation_form.cleaned_data['username'],
                password=user_creation_form.cleaned_data['password1']
            )
            messages.success(request, "¡Se ha creado tu cuenta correctamente.")
            login(request, user)
            return redirect('/')
    else:
        user_creation_form = CustomUserCreationForm()

    contexto = {
        'CustomUserCreationForm': user_creation_form
    }

    return render(request, "public/login/auth_register.html", contexto)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                messages.success(request, "¡Bienvenido! Has iniciado sesión correctamente.")
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Nombre de usuario o contraseña incorrectos.")
        else:
            messages.error(request, "Nombre de usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()

    return render(request, 'public/login/login.html', {'form': form})



@login_required
def listarPacientes(request):
    pacientes = Paciente.objects.all()
    contexto = {
            'pacientes': pacientes,
        }
    
    return render(request, "public/pacientes/lista_pacientes.html", contexto)


@login_required
def listarAtenciones(request):
    atenciones = ServicioSalud.objects.all()
    contexto = {
            'atenciones': atenciones,
        }
    
    return render(request, "public/servicioSalud/lista_atenciones.html", contexto)

@login_required
def crearPaciente(request):
    formPaciente = PacienteForm()
    
    if request.method == 'POST':
        formPaciente = PacienteForm(data=request.POST)
        if formPaciente.is_valid():
            nuevo_paciente =  formPaciente.save()

            pais_id = request.POST.get('CodigoPaisResidencia')
            if pais_id:
                pais = Pais.objects.get(codigo=pais_id)
                PacienteNacionalidad.objects.create(paciente=nuevo_paciente, pais=pais)
                messages.success(request, 'Paciente registrado con éxito.')
            return redirect('/')
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')


    return render(request, 'public/pacientes/crear_pacientes.html', {'FormPaciente': formPaciente})


@login_required
def crearAtencion(request):
    formAtencion = ServicioSaludForm()
    
    if request.method == 'POST':
        formAtencion = ServicioSaludForm(data=request.POST)
        if formAtencion.is_valid():
            nueva_atencion =  formAtencion.save()
            messages.success(request, 'Atención registrada con éxito.')
            return redirect('/listarAtenciones')
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')


    return render(request, 'public/servicioSalud/crear_atencion.html', {'FormAtencion': formAtencion})

@login_required
def eliminarPaciente(request, id):
    paciente = Paciente.objects.get(Id=id)
    paciente.delete()
    messages.success(request, 'Paciente eliminado con éxito')
    return redirect('/')

@login_required
def eliminarAtencion(request, id):
    atencion = ServicioSalud.objects.get(Id=id)
    atencion.delete()
    messages.success(request, 'Atención eliminada con éxito')
    return redirect('/listarAtenciones')

@login_required
def detallePaciente(request, id):
    paciente = Paciente.objects.get(Id=id)
    nacionalidades_asociadas = PacienteNacionalidad.objects.filter(paciente=paciente)
    discapacidades_asociadas = PacienteDiscapacidad.objects.filter(paciente=paciente)
    voluntad_anticipada = VoluntadAnticipada.objects.filter(paciente=paciente).first()
    oposicion = Oposicion.objects.filter(paciente=paciente).first()
    contexto = {'paciente': paciente,
                'discapacidades_asociadas': discapacidades_asociadas,
                'nacionalidades_asociadas': nacionalidades_asociadas,
                'voluntad_anticipada': voluntad_anticipada,
                'oposicion': oposicion,
                }
    return render(request, "public/pacientes/detalle_paciente.html", contexto)

@login_required
def detalleAtencion(request, id):
    atencion = ServicioSalud.objects.get(Id=id)
    contexto = {'atencion': atencion,
                }
    return render(request, "public/servicioSalud/detalle_atencion.html", contexto)

@login_required
def editarPaciente(request, id):
    paciente = get_object_or_404(Paciente, Id=id)

    nacionalidades_asociadas = PacienteNacionalidad.objects.filter(paciente=paciente)

    paises_disponibles = Pais.objects.exclude(pacientenacionalidad__paciente=paciente)

    discapacidades_asociadas = PacienteDiscapacidad.objects.filter(paciente=paciente)

    discapacidades_disponibles = Discapacidad.objects.exclude(pacientediscapacidad__paciente=paciente)

    voluntad_anticipada, created = VoluntadAnticipada.objects.get_or_create(paciente=paciente)

    oposicion, created = Oposicion.objects.get_or_create(paciente=paciente)

    if request.method == 'POST':
        if 'eliminar_discapacidad' in request.POST:
            discapacidad_id = request.POST.get('eliminar_discapacidad')
            discapacidad = get_object_or_404(Discapacidad, codigo=discapacidad_id)
            PacienteDiscapacidad.objects.filter(paciente=paciente, discapacidad=discapacidad).delete()
            return redirect('editarPaciente', id=paciente.Id)

        elif 'agregar_discapacidad' in request.POST:
            discapacidad_id = request.POST.get('paciente_discapacidad')
            discapacidad = get_object_or_404(Discapacidad, codigo=discapacidad_id)
            PacienteDiscapacidad.objects.create(paciente=paciente, discapacidad=discapacidad)
            return redirect('editarPaciente', id=paciente.Id)

        if 'eliminar_nacionalidad' in request.POST:
            pais_codigo = request.POST.get('eliminar_nacionalidad')
            pais = get_object_or_404(Pais, codigo=pais_codigo)
            PacienteNacionalidad.objects.filter(paciente=paciente, pais=pais).delete()
            return redirect('editarPaciente', id=paciente.Id)

        elif 'agregar_nacionalidad' in request.POST:
            pais_codigo = request.POST.get('nacionalidad_pais')
            pais = get_object_or_404(Pais, codigo=pais_codigo)
            PacienteNacionalidad.objects.create(paciente=paciente, pais=pais)
            return redirect('editarPaciente', id=paciente.Id)

        formPaciente = PacienteForm(request.POST, instance=paciente)
        if formPaciente.is_valid():
            formPaciente.save()
            voluntad_anticipada.voluntad = request.POST.get('voluntad')
            voluntad_anticipada.codigo_prestador = request.POST.get('codigo_prestador')
            voluntad_anticipada.fecha = timezone.now()
            voluntad_anticipada.save()

            oposicion.manifestacion = request.POST.get('oposicion')
            oposicion.fecha = timezone.now()
            oposicion.save()

            messages.success(request, 'Paciente actualizado con éxito.')
            return redirect('/') 

    else:
        formPaciente = PacienteForm(instance=paciente)

    contexto = {
        'FormPaciente': formPaciente,
        'paciente': paciente,
        'discapacidades_asociadas': discapacidades_asociadas,
        'discapacidades_disponibles': discapacidades_disponibles,
        'voluntad_anticipada': voluntad_anticipada,
        'oposicion': oposicion,
        'nacionalidades_asociadas': nacionalidades_asociadas,
        'paises_disponibles': paises_disponibles,
    }
    print(paciente.FechaNacimiento)
    return render(request, "public/pacientes/editar_paciente.html", contexto)


@login_required
def editarAtencion(request, id):
    atencion = get_object_or_404(ServicioSalud, Id=id)

    if request.method == 'POST':

        formAtencion = ServicioSaludForm(request.POST, instance=atencion)
        if formAtencion.is_valid():
            formAtencion.save()
            messages.success(request, 'Atención actualizada con éxito.')
            return redirect('/listarAtenciones') 
    else:
        formAtencion = ServicioSaludForm(instance=atencion)

    contexto = {
        'FormAtencion': formAtencion,
        'atencion': atencion,
    }

    return render(request, "public/servicioSalud/editar_atencion.html", contexto)

