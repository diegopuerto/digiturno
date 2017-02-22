from __future__ import unicode_literals
from account.models import Usuario
from django.db import models

class Turno(models.Model):
    turno = models.CharField(null=True, max_length=5, default=5)
    recepcionista = models.ForeignKey(Usuario,
                                      verbose_name="Persona que asigno la cita",
                                      related_name="recepcion_turnos")
    usuario = models.ForeignKey(Usuario,
                                verbose_name="Usuario al que se le asigna el turno",
                                related_name="usuario_turnos")
    asesor = models.ForeignKey(Usuario,
                               verbose_name="Asesor que atiende al Usuario en este turno", 
                               related_name="asesor_turnos", null=True)
    fecha_ingreso = models.DateTimeField(auto_now_add=True, null=True)
    fecha_inicio = models.DateTimeField(null=True)
    fecha_fin = models.DateTimeField(null=True)

    def __str__(self):
        return "No. %r" % (self.turno)

    def is_active(self):
            if self.fecha_inicio and not self.fecha_fin:
                return True
            else:
                return False


