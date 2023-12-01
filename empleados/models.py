from usuarios.models import Pais
from django.db import models

optionsC = [
    [1, 'Administrador de nivel'],
    [2, 'Asesor']
]

optionsN = [
    [1, 1],
    [2, 2],
    [3, 3]
]

class Empleado(models.Model):
    #Modelo de la tabla Empleado para la base de datos
    emp_id=models.AutoField(primary_key=True,unique=True)
    emp_nombre=models.CharField(max_length=15, verbose_name='Nombre del empleado')
    cargo=models.IntegerField(choices=optionsC, default=1)
    nivel=models.IntegerField(choices=optionsN, default=1)
    correo=models.CharField(max_length=40)
    contrase=models.CharField(max_length=15, verbose_name='contraseña', default='hdfdkalhf165516')
    id_pais=models.ForeignKey(Pais, on_delete=models.CASCADE)

    #Información principal de la tabla
    class Meta:
        db_table = 'Empleado'
        verbose_name = 'empleado'
        verbose_name_plural = 'empleados'

    def __str__(self):
        return self.emp_nombre