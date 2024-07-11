from django.db import models

# Create your models here.

class Multa(models.Model):
    Rut = models.CharField(primary_key=True, max_length=10)
    Vehiculo = models.CharField(max_length=6)
    Via_de_circulacion = models.CharField(max_length=50)
    tipo_de_infraccion = models.CharField(max_length=20)
    Monto = models.CharField(max_length=45)
    rut2 = models.CharField(max_length=10)
    Rol_inspector = models.CharField(max_length=50, blank=True, null=True)
    Descripcion_infraccion = models.CharField(max_length=50)
    Datos_sensor = models.CharField(max_length=50)

    def __str__(self):
        return str(self.Rut) + " " + str(self.Vehiculo)
