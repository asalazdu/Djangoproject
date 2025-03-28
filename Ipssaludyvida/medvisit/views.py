from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from .forms import PacienteForm, ServicioSaludForm
from django.utils import timezone



def home(request):
    pacientes = Paciente.objects.all()
    contexto = {
            'pacientes': pacientes,
        }
    
    return render(request, "public/pacientes/lista_pacientes.html", contexto)

def listarPacientes(request):
    pacientes = Paciente.objects.all()
    contexto = {
            'pacientes': pacientes,
        }
    
    return render(request, "public/pacientes/lista_pacientes.html", contexto)


def listarAtenciones(request):
    atenciones = ServicioSalud.objects.all()
    contexto = {
            'atenciones': atenciones,
        }
    
    return render(request, "public/servicioSalud/lista_atenciones.html", contexto)


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


def eliminarPaciente(request, id):
    paciente = Paciente.objects.get(Id=id)
    paciente.delete()
    messages.success(request, 'Paciente eliminado con éxito')
    return redirect('/')


def eliminarAtencion(request, id):
    atencion = ServicioSalud.objects.get(Id=id)
    atencion.delete()
    messages.success(request, 'Atención eliminada con éxito')
    return redirect('/listarAtenciones')

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


def detalleAtencion(request, id):
    atencion = ServicioSalud.objects.get(Id=id)
    contexto = {'atencion': atencion,
                }
    return render(request, "public/servicioSalud/detalle_atencion.html", contexto)


def editarPaciente(request, id):
    # Obtener el paciente
    paciente = get_object_or_404(Paciente, Id=id)

    # Obtener las nacionalidades asociadas al paciente
    nacionalidades_asociadas = PacienteNacionalidad.objects.filter(paciente=paciente)

    # Obtener todos los países que no están asociados al paciente
    paises_disponibles = Pais.objects.exclude(pacientenacionalidad__paciente=paciente)

    # Obtener discapacidades asociadas a este paciente
    discapacidades_asociadas = PacienteDiscapacidad.objects.filter(paciente=paciente)

    # Obtener discapacidades no asociadas al paciente
    discapacidades_disponibles = Discapacidad.objects.exclude(pacientediscapacidad__paciente=paciente)

    # Obtener o crear VoluntadAnticipada
    voluntad_anticipada, created = VoluntadAnticipada.objects.get_or_create(paciente=paciente)

    # Obtener o crear VoluntadAnticipada
    oposicion, created = Oposicion.objects.get_or_create(paciente=paciente)

    if request.method == 'POST':
        # Verificar si es una acción de eliminación o adición de discapacidad
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

        # Verificar si es una acción de eliminación o adición de nacionalidad
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

        # Si se trata de guardar cambios en el formulario del paciente
        formPaciente = PacienteForm(request.POST, instance=paciente)
        if formPaciente.is_valid():
            formPaciente.save()
            voluntad_anticipada.voluntad = request.POST.get('voluntad')
            voluntad_anticipada.codigo_prestador = request.POST.get('codigo_prestador')
            voluntad_anticipada.fecha = timezone.now()  # Asigna la fecha actual
            voluntad_anticipada.save()

            oposicion.manifestacion = request.POST.get('oposicion')
            oposicion.fecha = timezone.now()  # Asigna la fecha actual
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

    return render(request, "public/pacientes/editar_paciente.html", contexto)



def editarAtencion(request, id):
    # Obtener atencion
    atencion = get_object_or_404(ServicioSalud, Id=id)

    if request.method == 'POST':

        # Si se trata de guardar cambios en el formulario del paciente
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

