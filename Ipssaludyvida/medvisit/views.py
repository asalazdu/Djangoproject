from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from .forms import PacienteForm



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
    
    if request.method == 'POST':
        formPaciente = PacienteForm(request.POST, instance=paciente)
        if formPaciente.is_valid():
            formPaciente.save()
            messages.success(request, 'Paciente actualizado con éxito.')
            return redirect('/') 
    else:
        formPaciente = PacienteForm(instance=paciente)
    
    contexto = {'FormPaciente': formPaciente, 'paciente': paciente}
    return render(request, "public/pacientes/editar_paciente.html", contexto)