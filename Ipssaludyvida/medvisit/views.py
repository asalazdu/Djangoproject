from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from .forms import PacienteForm,ServicioSaludForm, PacienteDiscapacidadForm



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


def eliminarPaciente(request, id):
    paciente = Paciente.objects.get(Id=id)
    paciente.delete()
    messages.success(request, 'Paciente eliminado con éxito')
    return redirect('/')

def detallePaciente(request, id):
    paciente = Paciente.objects.get(Id=id)
    contexto = {'paciente': paciente}
    return render(request, "public/pacientes/detalle_paciente.html", contexto)

def editarPaciente(request, id):
    paciente = get_object_or_404(Paciente, Id=id)
    formPaciente = PacienteForm(instance=paciente)

    # Cargar discapacidades existentes
    discapacidades_existentes = PacienteDiscapacidad.objects.filter(paciente=paciente)

    # Cargar todas las discapacidades disponibles
    all_disabilities = Discapacidad.objects.all()

    if request.method == 'POST':
        # Actualizar datos del paciente
        formPaciente = PacienteForm(request.POST, instance=paciente)

        if formPaciente.is_valid():
            formPaciente.save()
            messages.success(request, 'Paciente actualizado con éxito.')

        # Manejar nuevas discapacidades
        if 'agregar_discapacidad' in request.POST:
            discapacidad_id = request.POST.get('discapacidad_id')
            discapacidad = get_object_or_404(Discapacidad, codigo=discapacidad_id)
            
            # Verificar si la discapacidad ya está registrada
            if not discapacidades_existentes.filter(discapacidad=discapacidad).exists():
                discapacidad_nueva = PacienteDiscapacidad(paciente=paciente, discapacidad=discapacidad)
                discapacidad_nueva.save()
                messages.success(request, 'Discapacidad agregada con éxito.')
            else:
                messages.warning(request, 'La discapacidad ya está registrada para este paciente.')

            return redirect('editarPaciente', id=paciente.id)  # Redirigir para evitar el reenvío de formulario

        




def CrearServicioSalud(request):
    formServicio = ServicioSaludForm()

    if request.method == 'POST':
        formServicio = ServicioSaludForm(request.POST)
        if formServicio.is_valid():
            formServicio.save()
            messages.success(request,'servicio de salud registrado correctamente.')
            return redirect('/')
        else:
            messages.error(request,'Porfavor corrige los errores del formulario.')

    return render(request,'public/Serviciosalud/crear_servicio_salud.html',{'formServicio':formServicio})


