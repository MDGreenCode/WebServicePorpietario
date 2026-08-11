from django.urls import path
from . import views

urlpatterns = [
    path('', views.crear_solicitud, name='crear_solicitud'),
    path('success/', views.success, name='success'),
    path('solicitudes/', views.listado_solicitudes, name='listado_solicitudes'),
    path('solicitudes/<int:pk>/', views.detalle_solicitud, name='detalle_solicitud'),
]
