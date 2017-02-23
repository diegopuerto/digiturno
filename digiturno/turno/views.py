from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Turno
from account.models import Usuario
from datetime import datetime, time
from django.utils.timezone import now

# Create your views here.
@login_required
def asignar(request, usuario_id ):
    def generacion_turno():
        hoy = now().date()
        hoy_inicio = datetime.combine(hoy, time())
        try:
            ultimo_turno_hoy = Turno.objects.filter(fecha_ingreso__gte=hoy_inicio).order_by('fecha_ingreso').last()
        except Exception as e:
            ultimo_turno_hoy = None
            print e

        if ultimo_turno_hoy == None:
            turno = 1
        else:
            turno = int(ultimo_turno_hoy.turno) + 1
        return turno
    turno = Turno(recepcionista=request.user.usuario,
                  usuario=Usuario.objects.get(id=usuario_id),
                 turno=generacion_turno())
    turno.save()
    turno_dos = Turno.objects.last()
    return HttpResponse('<h1>turno:%s</h1>'%turno_dos.turno)

def tomar(request):
    hoy = now().date()
    hoy_inicio = datetime.combine(hoy, time())
    try:
        turno = Turno.objects.filter(fecha_ingreso__gte=hoy_inicio).order_by('fecha_ingreso').filter(fecha_inicio=None).first()
        turno.asesor = request.user.usuario
        turno.fecha_inicio = now()
        turno.save()
    except Exception as e:
        return render(request,
                      'account/dashboard.html',
                      {'exception': e})
#    return HttpResponse('%r es el primer turno que voy a tomar'%turno.turno)
    return render(request,
                  'account/dashboard.html',
                  {'turno': turno,
                   'tomado': True,
                   'button': True})
                    
