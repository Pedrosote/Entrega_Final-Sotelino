from django.urls import path
from . import views

app_name = 'mensajes'

urlpatterns = [
    path('enviar/', views.enviar_mensaje, name='enviar_mensaje'),
    path('', views.lista_mensajes, name='lista_mensajes'),
]
