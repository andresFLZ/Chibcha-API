from rest_framework import viewsets, filters
from .serializer import MetodosDePagoSerializer
from .models import MetodosDePago

class MetodosDePagoView(viewsets.ModelViewSet):
    # Esta clase se encarga de manejar las solicitudes GET, POST, PUT, DELETE que lleguen a la api, esto lo hace usando viewsets
    
    serializer_class = MetodosDePagoSerializer
    queryset = MetodosDePago.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['id_usuario__id_usuario']