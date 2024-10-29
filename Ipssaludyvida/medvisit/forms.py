from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'CodigoTipoDocumento',
            'Identificacion',
            'PrimerApellido',
            'SegundoApellido',
            'PrimerNombre',
            'SegundoNombre',
            'FechaNacimiento',
            'HoraNacimiento',
            'CodigoSexo',
            'CodigoGenero',
            'CodigoOcupacion',
            'CodigoPaisResidencia',
            'CodigoMunicipio',
            'CodigoEtnia',
            'CodigoZonaResidencial',
            'CodigoEntidad',
        ]
        widgets = {
            'FechaNacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'HoraNacimiento': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }

        labels = {
            'CodigoTipoDocumento': 'Tipo de Documento',
            'Identificacion': 'Número de Identificación',
            'PrimerApellido': 'Primer Apellido',
            'SegundoApellido': 'Segundo Apellido',
            'PrimerNombre': 'Primer Nombre',
            'SegundoNombre': 'Segundo Nombre',
            'FechaNacimiento': 'Fecha de Nacimiento',
            'HoraNacimiento': 'Hora de Nacimiento',
            'CodigoSexo': 'Sexo',
            'CodigoGenero': 'Género',
            'CodigoOcupacion': 'Ocupación',
            'CodigoPaisResidencia': 'País de Residencia',
            'CodigoMunicipio': 'Municipio',
            'CodigoEtnia': 'Etnia',
            'CodigoZonaResidencial': 'Zona Residencial',
            'CodigoEntidad': 'Entidad',
        }

    def __init__(self, *args, **kwargs):
        super(PacienteForm, self).__init__(*args, **kwargs)
        self.fields['CodigoTipoDocumento'].empty_label = None
        self.fields['CodigoSexo'].empty_label = None
        self.fields['CodigoGenero'].empty_label = None
        self.fields['CodigoPaisResidencia'].empty_label = None
        self.fields['CodigoMunicipio'].empty_label = None
        self.fields['CodigoEtnia'].empty_label = None
        self.fields['CodigoZonaResidencial'].empty_label = None
        self.fields['CodigoEntidad'].empty_label = None
        self.fields['CodigoOcupacion'].empty_label = None

    def clean_Identificacion(self):
        Identificacion = self.cleaned_data.get('Identificacion')
        CodigoTipoDocumento = self.cleaned_data.get('CodigoTipoDocumento')

        if Paciente.objects.filter(Identificacion=Identificacion, CodigoTipoDocumento=CodigoTipoDocumento).exclude(Id=self.instance.Id).exists():
            raise forms.ValidationError("Ya existe un paciente con este número de documento y tipo de documento.")

        return Identificacion
    
class ServicioSaludForm(forms.ModelForm):
    class Meta:
        model = ServicioSalud
        fields = [
            'IdPaciente', 
            'CodigoPrestadoServicio', 
            'FechaHoraAtencion', 
            'CodigoModalidadRealizacion',
            'CodigoGrupoServicio', 
            'CodigoEntorno', 
            'CodigoViaIngreso', 
            'CodigoCausaMotivo',
            'ClasificacionTriage', 
            'CodigoDiagnostico', 
            'TipoDiagnosticoPrincipal'
        ]
        widgets = {
            'FechaHoraAtencion': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'IdPaciente': 'Paciente',
            'CodigoPrestadoServicio': 'Codigo Prestador',
            'FechaHoraAtencion': 'Fecha y Hora de Atención',
            'CodigoModalidadRealizacion': 'Modalidad de Atención',
            'CodigoGrupoServicio': 'Grupo de Servicios',
            'CodigoEntorno': 'Entorno',
            'CodigoViaIngreso': 'Via de Ingreso',
            'CodigoCausaMotivo': 'Causa de la Atención',
            'ClasificacionTriage': 'Triage',
            'CodigoDiagnostico': 'Diagnóstico',
            'TipoDiagnosticoPrincipal': 'Tipo de Diagnóstico',
        }


    def __init__(self, *args, **kwargs):
        super(ServicioSaludForm, self).__init__(*args, **kwargs)
        self.fields['IdPaciente'].empty_label = None
        self.fields['CodigoModalidadRealizacion'].empty_label = None
        self.fields['CodigoViaIngreso'].empty_label = None
        self.fields['CodigoCausaMotivo'].empty_label = None
        self.fields['CodigoDiagnostico'].empty_label = None
        self.fields['CodigoGrupoServicio'].choices = [(c[0], c[1]) for c in self.fields['CodigoGrupoServicio'].choices if c[0]]
        self.fields['CodigoEntorno'].choices = [(c[0], c[1]) for c in self.fields['CodigoEntorno'].choices if c[0]]
        self.fields['ClasificacionTriage'].choices = [(c[0], c[1]) for c in self.fields['ClasificacionTriage'].choices if c[0]]
        self.fields['TipoDiagnosticoPrincipal'].choices = [(c[0], c[1]) for c in self.fields['TipoDiagnosticoPrincipal'].choices if c[0]]
