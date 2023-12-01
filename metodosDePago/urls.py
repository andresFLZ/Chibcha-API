from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from .api import MetodosDePagoView

app_name = 'metodosPago' # Nombre de la aplicación, que sera llamada en otros archivos

# Genera todas las urls necesarias para las solicitudes GET, POST, PUT, DELETE
router = routers.DefaultRouter()
router.register(r'metodosDePago', MetodosDePagoView, 'metodosDePago')

urlpatterns = [
    #Rutas de la api de métodos de pago
    path("api/", include(router.urls)), 
]
