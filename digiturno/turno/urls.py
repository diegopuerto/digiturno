from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^asignar/(?P<usuario_id>\d+)?/$', views.asignar, name='asignar'),
    url(r'^cola/$', views.cola, name='cola'),
    url(r'^cambiar/$', views.cambiar, name='cambiar'),
    url(r'^tomar/$', views.tomar, name='tomar'),
    url(r'^tomar/(?P<turno_id>\d+)?/$', views.tomar, name='tomar'),
]
