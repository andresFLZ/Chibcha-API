from django.urls import path, include
from rest_framework import routers
from .api import DistribuidoresApiView, PagoComisionesApiView

app_name = 'distribuidores' # Nombre de la aplicación, que sera llamada en otros archivos

# Genera todas las urls necesarias para las solicitudes GET, POST, PUT, DELETE
router = routers.DefaultRouter()
router.register(r'distribuidores', DistribuidoresApiView, 'distribuidores') # Rutas para manejar las solicitudes GET, POST, DELETE
router.register(r'pagoComisiones', PagoComisionesApiView, 'pagoComisiones') # Rutas para manejar las solicitudes GET, POST, DELETE

urlpatterns = [
    #Rutas de la api de distribuidores
    path("api/", include(router.urls)), 
]