from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import DistribuidorSerializer, PagoComisionesSerializer
from.models import Distribuidor, PagoComisiones

class DistribuidoresApiView(viewsets.ModelViewSet):
    # Esta clase se encarga de manejar las solicitudes GET, POST, PUT, DELETE que lleguen a la api, esto lo hace usando viewsets
    
    serializer_class = DistribuidorSerializer
    queryset = Distribuidor.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['solicitud', 'id_distri', 'id_usuario']

class PagoComisionesApiView(viewsets.ModelViewSet):
    # Esta clase se encarga de manejar las solicitudes GET, POST, PUT, DELETE que lleguen a la api, esto lo hace usando viewsets
    
    serializer_class = PagoComisionesSerializer
    queryset = PagoComisiones.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_distri', 'pagado']