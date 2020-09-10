from django.urls import path
from . import views


app_name = 'usuarios'
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('usuarios/nuevo', views.registrar_usuario, name='registrar_usuario'),
    path('usuarios/cerrar_sesion', views.cerrar_sesion, name='cerrar_sesion'),
    path('usuarios/iniciar_sesion', views.iniciar_sesion, name='iniciar_sesion')
]
