from rest_framework import serializers
from .models import Usuarios,Paquetes,planPago

class UsuariosSerializer(serializers.ModelSerializer):
    #esta clase se encarga de tomar los datos del modelo usuario y transformarlos de sql a python y de python a json

    class Meta:
        # Se especifica que se desean incluir todos los campos del modelo Usuarios
        model = Usuarios
        fields = '__all__'

class ActualizarUsuariosSerializer(serializers.ModelSerializer):
    #Este serializer se encarga especificamente de manejar las solicitudes PUT
    
    class Meta:
        # Se especifica que se desean incluir todos los campos del modelo Usuarios
        model = Usuarios
        fields = '__all__'
        partial = True
        extra_kwargs = {
            'nombre': {'required': False},
            'telefono': {'required': False},
            'correo': {'required': False},
            'contrase': {'required': False},
            'id_pais': {'required': False},
        }
        
class ActualizarHostSerializer(serializers.ModelSerializer):
    #Este serializer se encarga especificamente de manejar las solicitudes PUT
    
    class Meta:
        # Se especifica que se desean incluir todos los campos del modelo Usuarios
        model = Usuarios
        partial = True
        fields = ['id_usuario', 'id_planPago', 'id_paquete']
        
class PaquetesHostSerializer(serializers.ModelSerializer):
    #esta clase se encarga de tomar los datos del modelo usuario y transformarlos de sql a python y de python a json

    class Meta:
        # Se especifica que se desean incluir todos los campos del modelo Plan
        model = Paquetes
        fields = '__all__'
        
class PlanesPagoSerializer(serializers.ModelSerializer):
    #esta clase se encarga de tomar los datos del modelo usuario y transformarlos de sql a python y de python a json

    class Meta:
        # Se especifica que se desean incluir todos los campos del modelo Usuarios
        model = planPago
        fields = '__all__'
        
