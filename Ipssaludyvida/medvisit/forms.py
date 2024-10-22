from django import forms
from .models import *

class PacienteDiscapacidadForm(forms.ModelForm):
    class Meta:
        model = PacienteDiscapacidad
        fields = ['discapacidad']
        labels = {
            'discapacidad': 'Discapacidad',
        }

class PacienteForm(forms.ModelForm):
    discapacidad = forms.ModelMultipleChoiceField(
        queryset=Discapacidad.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Discapacidades'
    )
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

        # Si el paciente ya existe (es una edición)
        if self.instance.pk:
            # Obtiene todas las discapacidades asociadas al paciente usando el modelo intermedio PacienteDiscapacidad
            discapacidades = PacienteDiscapacidad.objects.filter(paciente=self.instance).values_list('discapacidad', flat=True)
            self.fields['discapacidad'].initial = discapacidades

    def clean_Identificacion(self):
        Identificacion = self.cleaned_data.get('Identificacion')
        CodigoTipoDocumento = self.cleaned_data.get('CodigoTipoDocumento')

        # Verifica si ya existe un paciente con el mismo número de documento
        if Paciente.objects.filter(Identificacion=Identificacion, CodigoTipoDocumento=CodigoTipoDocumento).exclude(Id=self.instance.Id).exists():
            raise forms.ValidationError("Ya existe un paciente con este número de documento y tipo de documento.")

        return Identificacion
    
    def save(self, commit=True):
        instance = super(PacienteForm, self).save(commit=False)
        if commit:
            instance.save()
            self.save_m2m()

            # Guardar las discapacidades seleccionadas
            discapacidades = self.cleaned_data['discapacidad']
            PacienteDiscapacidad.objects.filter(paciente=instance).delete()  # Limpiar las discapacidades anteriores
            for discapacidad in discapacidades:
                PacienteDiscapacidad.objects.create(paciente=instance, discapacidad=discapacidad)

        return instance

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
            'FechaHoraAtencion': forms.DateTimeInput(attrs={'type': 'datetime-local','class': 'form-control'}),
        }

        labels = {
            'IdPaciente':'Paciente',
            'CodigoPrestadoServicio':'Codigo prestado de servicio',
            'FechaHoraAtencion':'Fecha y hora de atencion',
            'CodigoModalidadRealizacion':'Modalidad de realizacion',
            'CodigoGrupoServicio':'Grupo de servicio',
            'CodigoEntorno':'Entorno',
            'CodigoViaIngreso':'Via de Ingreso',
            'CodigoCausaMotivo':'Causa o motivo',
            'ClasificacionTriage':'Triage',
            'CodigoDiagnostico':'Diagnostico',
            'TipoDiagnosticoPrincipal':'Tipo de diagnostico principal',
        }
    
    def __init__(self, *args, **kwargs):
        super(ServicioSaludForm, self).__init__(*args, **kwargs)   
        self.fields['IdPaciente'].empty_label = None
        self.fields['CodigoPrestadoServicio'].empty_label = None
        self.fields['FechaHoraAtencion'].empty_label = None 
        self.fields['CodigoModalidadRealizacion'].empty_label = None
        self.fields['CodigoGrupoServicio'].empty_label = None
        self.fields['CodigoEntorno'].empty_label = None
        self.fields['ClasificacionTriage'].empty_label = None
        self.fields['CodigoDiagnostico'].empty_label = None
        self.fields['CodigoViaIngreso'].empty_label = None
        self.fields['CodigoCausaMotivo'].empty_label = None 
        self.fields['TipoDiagnosticoPrincipal'].empty_label = None

