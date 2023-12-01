from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from .api import DominiosApiView, facturasApiView

app_name = 'dominios' # Nombre de la aplicación, que sera llamada en otros archivos

# Genera todas las urls necesarias para las solicitudes GET, POST, PUT, DELETE
router = routers.DefaultRouter()
router.register(r'dominios', DominiosApiView, 'dominios')
router.register(r'facturas', facturasApiView, 'facturas')

urlpatterns = [
    path("api/", include(router.urls)), 
]