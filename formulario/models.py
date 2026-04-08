from django.db import models



class Solicitud(models.Model):

    TIPO_IDENTIFICACION = [
        ('cedula', 'Cédula'),
        ('pasaporte', 'Pasaporte'),
    ]

    SEXO = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]

    ESTADO_CIVIL = [
        ('soltero', 'Soltero'),
        ('casado', 'Casado'),
        ('divorciado', 'Divorciado'),
        ('union_libre', 'Unión Libre'),
        ('viudo', 'Viudo'),
    ]

    nombres_apellidos = models.CharField(max_length=200)
    tipo_identificacion = models.CharField(max_length=20, choices=TIPO_IDENTIFICACION)
    numero_identificacion = models.CharField(max_length=50)

    sexo = models.CharField(max_length=1, choices=SEXO)
    nacionalidad = models.CharField(max_length=100)

    fecha_nacimiento = models.DateField()
    lugar_nacimiento = models.CharField(max_length=150)
    tipo_sangre = models.CharField(max_length=5)

    estado_civil = models.CharField(max_length=20, choices=ESTADO_CIVIL)
    fecha_matrimonio = models.DateField(null=True, blank=True)
    empleado_recomendador = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nombres_apellidos
    
class Educacion(models.Model):
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE, related_name='educaciones')

    nivel = models.CharField(max_length=100)
    institucion = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titulo

class Experiencia(models.Model):
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE, related_name='experiencias')

    empresa = models.CharField(max_length=200)
    puesto = models.CharField(max_length=150)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.empresa