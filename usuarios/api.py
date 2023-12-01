from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters, viewsets
from .serializer import UsuariosSerializer, ActualizarUsuariosSerializer,PaquetesHostSerializer,PlanesPagoSerializer,ActualizarHostSerializer
from .models import Usuarios,Paquetes,planPago

class UsuariosApiView(viewsets.ModelViewSet):
    # Esta clase se encarga de manejar las solicitudes GET, POST, PUT, DELETE que lleguen a la api, esto lo hace usando viewsets

    serializer_class = UsuariosSerializer
    queryset = Usuarios.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['correo', 'id_usuario']

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ActualizarUsuariosApiView(viewsets.ModelViewSet):
    serializer_class = ActualizarUsuariosSerializer
    queryset = Usuarios.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['correo']

    # Sobrescribe los métodos que no necesitas
    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
class PaquetesHostApiView(viewsets.ModelViewSet):
    serializer_class = PaquetesHostSerializer
    queryset = Paquetes.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['id_paquete']
    
    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
class PlanesPagoApiView(viewsets.ModelViewSet):
    serializer_class = PlanesPagoSerializer
    queryset = planPago.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['id_planPago']
    
    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class actualizarHostSeleccionApiView(viewsets.ModelViewSet):
    serializer_class= ActualizarHostSerializer
    filter_backends = [filters.SearchFilter]
    queryset = Usuarios.objects.all()
    search_fields = ['id_usuario']
    
     # Sobrescribe los métodos que no necesitas
    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)