from django import forms
from .models import *


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

        # Verifica si ya existe un paciente con el mismo número de documento
        if Paciente.objects.filter(Identificacion=Identificacion, CodigoTipoDocumento=CodigoTipoDocumento).exclude(Id=self.instance.Id).exists():
            raise forms.ValidationError("Ya existe un paciente con este número de documento y tipo de documento.")

        return Identificacion
