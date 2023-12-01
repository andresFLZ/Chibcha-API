from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import EmpleadosSerializer
from.models import Empleado

class EmpleadosApiView(viewsets.ModelViewSet):
    # Esta clase se encarga de manejar las solicitudes GET, POST, PUT, DELETE que lleguen a la api, esto lo hace usando viewsets

    serializer_class = EmpleadosSerializer
    queryset = Empleado.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['correo', 'nivel', 'cargo']