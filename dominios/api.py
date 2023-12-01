from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import DominiosSerializer, facturasSerializer
from .models import Dominios, facturas

class DominiosApiView(viewsets.ModelViewSet):
    # Esta clase se encarga de manejar las solicitudes GET, POST, PUT, DELETE que lleguen a la api, esto lo hace usando viewsets

    serializer_class = DominiosSerializer
    queryset = Dominios.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_dom', 'solicitud', 'id_usuario', 'paginaWeb', 'nombre_dom']

class facturasApiView(viewsets.ModelViewSet):
    # Esta clase se encarga de manejar las solicitudes GET, POST, PUT, DELETE que lleguen a la api, esto lo hace usando viewsets

    serializer_class = facturasSerializer
    queryset = facturas.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_factura', 'id_metodoDePago', 'd_dom']

