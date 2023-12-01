from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import TicketsSerializer
from .models import Tickets

class TicketsView(viewsets.ModelViewSet):
    # Esta clase se encarga de manejar las solicitudes GET, POST, PUT, DELETE que lleguen a la api, esto lo hace usando viewsets
    
    serializer_class = TicketsSerializer
    queryset = Tickets.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tipoTicket', 'id_empleado', 'revisado']