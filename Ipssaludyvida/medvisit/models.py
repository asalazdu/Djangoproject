from django.db import models

# Create your models here.
from django.db import models

class CausaMotivo(models.Model):
    codigo = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'CausaMotivo'


class Departamento(models.Model):
    codigo = models.CharField(max_length=5, primary_key=True)
    codigo_pais = models.CharField(max_length=3)
    nombre_departamento = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'Departamento'


class Diagnostico(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    nombre = models.CharField(max_length=300, null=True, blank=True)
    codigo_padre = models.CharField(max_length=4, null=True, blank=True)

    class Meta:
        db_table = 'Diagnostico'


class Discapacidad(models.Model):
    codigo = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'Discapacidad'


class Entidad(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=200)

    class Meta:
        db_table = 'Entidad'


class Etnia(models.Model):
    codigo = models.CharField(max_length=5, primary_key=True)
    nombre = models.CharField(max_length=150)

    class Meta:
        db_table = 'Etnia'


class Genero(models.Model):
    codigo = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        db_table = 'Genero'


class ModalidadRealizacion(models.Model):
    codigo = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'ModalidadRealizacion'


class Municipio(models.Model):
    codigo = models.CharField(max_length=5, primary_key=True)
    codigo_departamento = models.CharField(max_length=5)
    nombre = models.CharField(max_length=200)

    class Meta:
        db_table = 'Municipio'


class Ocupacion(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    nombre = models.CharField(max_length=200, null=True, blank=True)
    codigo_padre = models.CharField(max_length=4, null=True, blank=True)

    class Meta:
        db_table = 'Ocupacion'


class Oposicion(models.Model):
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)
    manifestacion = models.CharField(max_length=2)
    fecha = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'Oposicion'
        unique_together = ('paciente', 'manifestacion')

class PacienteDiscapacidad(models.Model):
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)
    discapacidad = models.ForeignKey(Discapacidad, on_delete=models.CASCADE)

    class Meta:
        db_table = 'PacienteDiscapacidad'
        unique_together = ('paciente', 'discapacidad')


class PacienteDiagnostico(models.Model):
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)
    diagnostico = models.ForeignKey(Diagnostico, on_delete=models.CASCADE)

    class Meta:
        db_table = 'PacienteDiagnostico'
        unique_together = ('paciente', 'diagnostico')


class PacienteNacionalidad(models.Model):
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)
    pais = models.ForeignKey('Pais', on_delete=models.CASCADE)

    class Meta:
        db_table = 'PacienteNacionalidad'
        unique_together = ('paciente', 'pais')


class Pais(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'Pais'


class Sexo(models.Model):
    codigo = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=50, null=True, blank=True)
    class Meta:
        db_table = 'Sexo'


class TipoDocumento(models.Model):
    codigo = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=50, null=True, blank=True)
    class Meta:
        db_table = 'TipoDocumento'




class ViaIngreso(models.Model):
    codigo = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'ViaIngreso'


class VoluntadAnticipada(models.Model):
    id = models.AutoField(primary_key=True)
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)
    voluntad = models.CharField(max_length=2, null=True, blank=True)
    fecha = models.DateTimeField(null=True, blank=True)
    codigo_prestador = models.CharField(max_length=12, null=True, blank=True)

    class Meta:
        db_table = 'VoluntadAnticipada'


class ZonaResidencial(models.Model):
    codigo = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'ZonaResidencial'


class Paciente(models.Model):
    Id = models.AutoField(primary_key=True)
    CodigoTipoDocumento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    Identificacion = models.CharField(max_length=20)
    PrimerApellido = models.CharField(max_length=50)
    SegundoApellido = models.CharField(max_length=50, blank=True, null=True)
    PrimerNombre = models.CharField(max_length=50)
    SegundoNombre = models.CharField(max_length=50, blank=True, null=True)
    FechaNacimiento = models.DateField()
    HoraNacimiento = models.TimeField(blank=True, null=True)
    CodigoSexo = models.ForeignKey(Sexo, on_delete=models.CASCADE)
    CodigoGenero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    CodigoOcupacion = models.ForeignKey(Ocupacion, on_delete=models.CASCADE)
    CodigoPaisResidencia = models.ForeignKey(Pais, on_delete=models.CASCADE)
    CodigoMunicipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    CodigoEtnia = models.ForeignKey(Etnia, on_delete=models.CASCADE)
    CodigoZonaResidencial = models.ForeignKey(ZonaResidencial, on_delete=models.CASCADE)
    CodigoEntidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)