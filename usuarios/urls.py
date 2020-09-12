from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'usuarios'
urlpatterns = [
    path('usuarios/', views.inicio, name='inicio'),
    path('usuarios/nuevo', views.registrar_usuario, name='registrar_usuario'),
    path('usuarios/cerrar_sesion', views.cerrar_sesion, name='cerrar_sesion'),
    path('usuarios/iniciar_sesion', views.iniciar_sesion, name='iniciar_sesion'),
    path('accounts/register/', views.register_view, name='register'),
    path('accounts/cambiar-password', auth_views.PasswordResetView.as_view()),
    path('accounts/cambiar-password-hecho', auth_views.PasswordChangeDoneView.as_view()),
    path('accounts/confirmar-cambiar-password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view()),
    path('accounts/cambiar-password-completado', auth_views.PasswordResetCompleteView.as_view()),
]
