from django.urls import path, include
from rest_framework import routers
from .api import EmpleadosApiView

app_name = 'empleados' # Nombre de la aplicación, que sera llamada en otros archivos

# Genera todas las urls necesarias para las solicitudes GET, POST, PUT, DELETE
router = routers.DefaultRouter()
router.register(r'empleados', EmpleadosApiView, 'empleados') # Rutas para manejar las solicitudes GET, POST, DELETE

urlpatterns = [
    #Rutas de la api de empleados
    path("api/", include(router.urls)), # Se incluyen todas las urls GET, POST, PUT, DELETE para interactuar con el api
]