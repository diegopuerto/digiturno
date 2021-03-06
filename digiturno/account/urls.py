from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #previous views
    #url(r'^login/$', views.user_login, name='login'),
    # login / logout urls
    url(r'^login/$',
        auth_views.login,
        name='login'),
    url(r'^logout/$',
        auth_views.logout,
        name='logout'),
    url(r'^logout-then-login/$',
        auth_views.logout_then_login,
       name='logout_then_login'),
    url(r'^$', views.dashboard, name='dashboard'),
#    url(r'^verificacion/$', views.dashboard, name='verificacion'),
    url(r'^registro/$', views.registro, name='registro'),
    url(r'^cedula/$', views.dashboard, name='ajax_dashboard'),
]
