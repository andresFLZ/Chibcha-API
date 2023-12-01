from rest_framework import serializers
from .models import MetodosDePago

class MetodosDePagoSerializer(serializers.ModelSerializer):
     #esta clase se encarga de tomar los datos del modelo metodosDePago y transformarlos de sql a python y de python a json
     
     class Meta:
           # Se especifica que se desean incluir todos los campos del modelo MetodosDePago
           model = MetodosDePago
           fields = '__all__'