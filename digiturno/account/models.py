from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Usuario(models.Model):
    ROLES = (
        ('recepcion', 'Recepcion'),
        ('atencion', 'Atencion'),
        ('admin', 'Administrativo'),
        ('usuario', 'Usuario'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=20,
                          choices=ROLES,
                          default='atencion')
    cedula = models.CharField(null=True, max_length=20)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "%r" % (self.user.username)
