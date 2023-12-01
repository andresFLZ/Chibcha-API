from rest_framework import serializers
from . models import Empleado

class EmpleadosSerializer(serializers.ModelSerializer):
    #esta clase se encarga de tomar los datos del modelo empleados y transformarlos de sql a python y de python a json

    class Meta:
        # Se especifica que se desean incluir todos los campos del modelo Empleado
        model = Empleado
        fields = '__all__'