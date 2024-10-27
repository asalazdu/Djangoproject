from django.contrib import admin
from .models import (
    CausaMotivo,
    Departamento,
    Diagnostico,
    Discapacidad,
    Entidad,
    Etnia,
    Genero,
    ModalidadRealizacion,
    Municipio,
    Ocupacion,
    Oposicion,
    Paciente,
    PacienteDiscapacidad,
    PacienteNacionalidad,
    Pais,
    Sexo,
    TipoDocumento,
    ViaIngreso,
    VoluntadAnticipada,
    ZonaResidencial,
    ServicioSalud,
)

# Registro de modelos
admin.site.register(CausaMotivo)
admin.site.register(Departamento)
admin.site.register(Diagnostico)
admin.site.register(Discapacidad)
admin.site.register(Entidad)
admin.site.register(Etnia)
admin.site.register(Genero)
admin.site.register(ModalidadRealizacion)
admin.site.register(Municipio)
admin.site.register(Ocupacion)
admin.site.register(Oposicion)
admin.site.register(Paciente)
admin.site.register(PacienteDiscapacidad)
admin.site.register(PacienteNacionalidad)
admin.site.register(Pais)
admin.site.register(Sexo)
admin.site.register(TipoDocumento)
admin.site.register(ViaIngreso)
admin.site.register(VoluntadAnticipada)
admin.site.register(ZonaResidencial)
admin.site.register(ServicioSalud)
