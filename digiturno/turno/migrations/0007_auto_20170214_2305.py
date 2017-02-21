# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 23:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turno', '0006_auto_20170214_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turno',
            name='estado',
        ),
        migrations.AlterField(
            model_name='turno',
            name='asesor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asesor_turnos', to=settings.AUTH_USER_MODEL, verbose_name='Asesor que atiende al Usuario en este turno'),
        ),
        migrations.AlterField(
            model_name='turno',
            name='fecha_fin',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='turno',
            name='fecha_inicio',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='turno',
            name='recepcionista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recepcion_turnos', to=settings.AUTH_USER_MODEL, verbose_name='Persona que asigno la cita'),
        ),
        migrations.AlterField(
            model_name='turno',
            name='turno',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='turno',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='usuario_turnos', to=settings.AUTH_USER_MODEL, verbose_name='Usuario al que se le asigna el turno'),
            preserve_default=False,
        ),
    ]
