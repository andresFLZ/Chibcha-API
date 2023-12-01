from rest_framework import serializers
from .models import Tickets

class TicketsSerializer(serializers.ModelSerializer):
     #esta clase se encarga de tomar los datos del modelo tickets y transformarlos de sql a python y de python a json
     
     class Meta:
           # Se especifica que se desean incluir todos los campos del modelo Tickets
           model = Tickets
           fields = '__all__'