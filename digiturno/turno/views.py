from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
@login_required
def asignar(request, usuario_id ):
    return HttpResponse('Este es el usuario al que le vamos a asignar el turno:%r' % (usuario_id))

def cola(request):
    return render(request,'turno/cola.html')

@login_required
def cambiar(request):
    user = request.user
    return render(request,'turno/cambiar.html', {'user':user})
