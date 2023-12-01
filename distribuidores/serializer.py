from rest_framework import serializers
from .models import Distribuidor, PagoComisiones

class DistribuidorSerializer(serializers.ModelSerializer):
    #esta clase se encarga de tomar los datos del modelo distribuidor y transformarlos de sql a python y de python a json

    class Meta:
        # Se especifica que se desean incluir todos los campos del modelo Distribuidor
        model = Distribuidor
        fields = '__all__'

class PagoComisionesSerializer(serializers.ModelSerializer):
    #esta clase se encarga de tomar los datos del modelo pagosComision y transformarlos de sql a python y de python a json

    class Meta:
        # Se especifica que se desean incluir todos los campos del modelo Distribuidor
        model = PagoComisiones
        fields = '__all__'