from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
@login_required
def asignar(request, usuario_id ):
        return HttpResponse('Este es el usuario al que le vamos a asignar el turno:%r' % (usuario_id))
