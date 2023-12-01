from rest_framework import serializers
from .models import Dominios, facturas

class DominiosSerializer(serializers.ModelSerializer):
    #esta clase se encarga de tomar los datos del modelo dominios y transformarlos de sql a python y de python a json

    class Meta:
        # Se especifica que se desean incluir todos los campos del modelo Dominios
        model = Dominios
        fields = '__all__'

class facturasSerializer(serializers.ModelSerializer):
    #esta clase se encarga de tomar los datos del modelo facturas y transformarlos de sql a python y de python a json

    class Meta:
        # Se especifica que se desean incluir todos los campos del modelo facturas
        model = facturas
        fields = '__all__'