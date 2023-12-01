from empleados.models import Empleado
from usuarios.models import Usuarios
from django.db import models

optionsT = [
    [1, 'Nivel 1'],
    [2, 'Nivel 2'],
    [3, 'Nivel 3']
]

class Tickets(models.Model):
    #Modelo de la tabla Tickets para la base de datos
    id_Ticket=models.AutoField(primary_key=True,unique=True)
    tipoTicket=models.IntegerField(choices=optionsT, default=1, verbose_name='Tipo de ticket')
    titulo=models.CharField(max_length=40, default='Titulo ticket')
    mensaje=models.TextField(max_length=500)
    revisado=models.BooleanField(default=False)
    id_usuario=models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    id_empleado=models.ForeignKey(Empleado, on_delete=models.CASCADE, blank=True, null=True, default=None)

    #Información principal de la tabla
    class Meta:
        db_table = 'Tickets'
        verbose_name = 'ticket'
        verbose_name_plural = 'tickets'

    def __str__(self):
        return self.id_Ticket + ' ' + self.tipoTicket
