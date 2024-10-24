from django.db import models

class CausaMotivo(models.Model):
    codigo = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'CausaMotivo'

    def __str__(self):
        return self.nombre


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

    def __str__(self):
        return self.nombre


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

    def __str__(self):
        return self.nombre


class Etnia(models.Model):
    codigo = models.CharField(max_length=5, primary_key=True)
    nombre = models.CharField(max_length=150)

    class Meta:
        db_table = 'Etnia'

    def __str__(self):
        return self.nombre


class Genero(models.Model):
    codigo = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        db_table = 'Genero'
    
    def __str__(self):
        return self.nombre


class ModalidadRealizacion(models.Model):
    codigo = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'ModalidadRealizacion'

    def __str__(self):
        return self.nombre


class Municipio(models.Model):
    codigo = models.CharField(max_length=5, primary_key=True)
    codigo_departamento = models.CharField(max_length=5)
    nombre = models.CharField(max_length=200)

    class Meta:
        db_table = 'Municipio'
    
    def __str__(self):
        return self.nombre


class Ocupacion(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    nombre = models.CharField(max_length=200, null=True, blank=True)
    codigo_padre = models.CharField(max_length=4, null=True, blank=True)

    class Meta:
        db_table = 'Ocupacion'

    def __str__(self):
        return self.nombre
    
    


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

    def __str__(self):
        return self.nombre


class Sexo(models.Model):
    codigo = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=50, null=True, blank=True)
    class Meta:
        db_table = 'Sexo'

    def __str__(self):
        return self.nombre


class TipoDocumento(models.Model):
    codigo = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=50, null=True, blank=True)
    class Meta:
        db_table = 'TipoDocumento'

    def __str__(self):
        return self.nombre




class ViaIngreso(models.Model):
    codigo = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'ViaIngreso'

    def __str__(self):
        return self.nombre


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

    def __str__(self):
        return self.nombre


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

    class Meta:
        db_table = 'Paciente'

    def __str__(self):
        # Combinar identificación y nombre completo del paciente
        nombres = f"{self.PrimerNombre} {self.SegundoNombre}" if self.SegundoNombre else self.PrimerNombre
        apellidos = f"{self.PrimerApellido} {self.SegundoApellido}" if self.SegundoApellido else self.PrimerApellido
        nombre_completo = f"{nombres} {apellidos}"
        return f"{nombre_completo}"


class ServicioSalud(models.Model):
    GRUPO_SERVICIOS_CHOICES = [
        ('01', 'Consulta externa'),
        ('02', 'Apoyo diagnostico y complementacion terapeutica'),
        ('03', 'Internación'),
        ('04', 'Quirurgico'),
        ('05', 'Atencion Inmediata'),
    ]

    ENTORNO_CHOICES = [
        ('01', 'Hogar'),
        ('02', 'Comunitario'),
        ('03', 'Escolar'),
        ('04', 'Laboral'),
        ('05', 'Institucional'),
    ]

    TRIAGE_CHOICES = [
        ('01', 'Triage I'),
        ('02', 'Triage II'),
        ('03', 'Triage III'),
        ('04', 'Triage IV'),
        ('05', 'Triage V'),
    ]

    TIPO_DIAGNOSTICO_CHOICES = [
        ('01', 'Impresión diagnostica'),
        ('02', 'Confirmado nuevo'),
        ('03', 'Confirmado repetido'),
    ]

    Id = models.AutoField(primary_key=True)
    IdPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    CodigoPrestadoServicio = models.CharField(max_length=100)
    FechaHoraAtencion = models.DateTimeField()
    CodigoModalidadRealizacion = models.ForeignKey(ModalidadRealizacion, on_delete=models.CASCADE)
    CodigoGrupoServicio = models.CharField(max_length=100, choices=GRUPO_SERVICIOS_CHOICES)
    CodigoEntorno = models.CharField(max_length=100, choices=ENTORNO_CHOICES)
    CodigoViaIngreso = models.ForeignKey(ViaIngreso, on_delete=models.CASCADE)
    CodigoCausaMotivo = models.ForeignKey(CausaMotivo, on_delete=models.CASCADE)
    ClasificacionTriage = models.CharField(max_length=100, choices=TRIAGE_CHOICES)
    CodigoDiagnostico = models.ForeignKey(Diagnostico, on_delete=models.CASCADE)
    TipoDiagnosticoPrincipal = models.CharField(max_length=100, choices=TIPO_DIAGNOSTICO_CHOICES)

    class Meta:
        db_table = 'ServicioSalud'