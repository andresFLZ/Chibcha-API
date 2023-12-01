from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from .api import UsuariosApiView, ActualizarUsuariosApiView,PaquetesHostApiView,PlanesPagoApiView, actualizarHostSeleccionApiView

app_name = 'usuarios' # Nombre de la aplicación, que sera llamada en otros archivos

# Genera todas las urls necesarias para las solicitudes GET, POST, PUT, DELETE
router = routers.DefaultRouter()
router.register(r'usuarios', UsuariosApiView, 'usuarios') # Rutas para manejar las solicitudes GET, POST, DELETE
router.register(r'paquetes', PaquetesHostApiView, 'paquetes') # Rutas para manejar las solicitudes GET, POST, DELETE
router.register(r'planPago', PlanesPagoApiView, 'PlanPago') # Rutas para manejar las solicitudes GET, POST, DELETE
router.register(r'aceptarHost', actualizarHostSeleccionApiView, basename='aceptarHost') # Rutas para manejar las solicitudes PUT
router.register(r'actualizar_usuarios', ActualizarUsuariosApiView, basename='actualizar_usuarios') # Ruta para manejar las solicitudes PUT

urlpatterns = [
    #Rutas de la api de usuarios
    path("usuarios/api/", include(router.urls)),
]
