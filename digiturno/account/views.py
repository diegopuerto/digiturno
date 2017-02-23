"""
from django.contrib.auth import authenticate, login
from .forms import LoginForm
"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import IdentificacionForm, InfoUsuarioForm, InfoUserForm, RegistroForm
from .models import Usuario
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

@login_required
@csrf_exempt
def dashboard(request):
                
    if request.method == 'POST':
        print ("request.post: %s"%request.POST)
        if request.is_ajax():
            form = IdentificacionForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                try:
                    usuario = Usuario.objects.get(cedula=cd['cedula'])
                except Exception as e:
                    #return HttpResponse("<h1>El usuario no existe: %s</h1>" % (e))
                    return render(request,
                                  'account/not_found_user.html',
                                  {'exception': e},
                                  status = 201 
                                  )
                user = usuario.user
                if usuario:
                    form_uno = InfoUsuarioForm(instance = usuario)
                    form_dos = InfoUserForm(instance = user)
                    return render(request,
                                  'account/dashboard.html',
                                  {'section': 'dashboard',
                                   'form_uno': form_uno, 
                                   'form_dos': form_dos,
                                   'no_submit':True,
                                   'turno': True,
                                   'usuario': usuario})
                else:
                    return render(request,
                                  'account/dashboard.html',
                                  {'section': 'dashboard',
                                   'form': form})
    else:
        form = IdentificacionForm() 
        return render(request,
                      'account/dashboard.html',
                      {'section': 'dashboard',
                       'form': form})
    
@login_required
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                user = User.objects.create_user(cd['nombre'], email=cd['correo'])
            except Exception as e:
                form = RegistroForm()
                return render(request,
                             'account/registro.html',
                              {'mensaje': 'Ya existe un usuario con el nombre:',
                               'nombre': cd['nombre'],
                               'excepcion': e,
                               'form': form })
            usuario = Usuario(user=user, rol='usuario', cedula=cd['cedula'])
            try:
                usuario.save()
                return render(request, 
                              'account/registro.html',
                              {'form': form,
                               'no_submit': True,
                               'mensaje': 'Se ha registrado exitosamente al usuario',
                               'nombre': cd['nombre'],
                               'turno': True})
            except Exception as e:
                form = RegistroForm()
                return render(request,
                             'account/registro.html',
                              {'mensaje': 'No se ha podido registrar al usuario',
                               'nombre': cd['nombre'],
                               'form': form})
    else:
        form = RegistroForm()
        return render(request, 
                    'account/registro.html',
                    {'form': form})
