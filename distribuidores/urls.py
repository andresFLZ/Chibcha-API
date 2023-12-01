from django.urls import path, include
from rest_framework import routers
from .views import InicioDistribuidoresView, SolicitudDistribuidorView, PerfilDistribuidorView, ListarRecibosCobroView, DetalleReciboCobroView, PagoReciboCobroView
from .api import DistribuidoresApiView, PagoComisionesApiView

app_name = 'distribuidores' # Nombre de la aplicación, que sera llamada en otros archivos

# Genera todas las urls necesarias para las solicitudes GET, POST, PUT, DELETE
router = routers.DefaultRouter()
router.register(r'distribuidores', DistribuidoresApiView, 'distribuidores') # Rutas para manejar las solicitudes GET, POST, DELETE
router.register(r'pagoComisiones', PagoComisionesApiView, 'pagoComisiones') # Rutas para manejar las solicitudes GET, POST, DELETE

urlpatterns = [
    #Rutas de la api de distribuidores
    path("api/", include(router.urls)), # Se incluyen todas las urls GET, POST, PUT, DELETE para interactuar con el api
    #Rutas de la página de distribuidores
    path('', InicioDistribuidoresView.as_view(), name='DistribuidoresInicio'), # Ruta de la página principal de la sección de distribuidores
    path('solicitud/', SolicitudDistribuidorView.as_view(), name='SolicitudDistribuidor'), # Ruta de la página donde el cliente realizara la solicitud para ser un distribuidor
    path('perfil/', PerfilDistribuidorView.as_view(), name='PerfilDistribuidor'), # Ruta de la página donde el administrador de distribuidor puede ver su perfil como distribuidor
    path("recibos/lista/", ListarRecibosCobroView.as_view(), name='ListarRecibosCobro'), # Página donde se listaran los recibos de cobro que le llegan a un administrador de un distribuidor
    path('recibos/<int:pk>/', DetalleReciboCobroView.as_view(), name='DetalleReciboCobro'), # Ruta de la página donde un distribuidor puede ver a detalle un recibo
    path('recibos/pagar/', PagoReciboCobroView.as_view(), name='PagoReciboCobro'), # Ruta de redirección donde se realiza la lógica de pago de comisión por parte de un distribuidor
]