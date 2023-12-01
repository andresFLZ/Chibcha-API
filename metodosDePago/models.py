from django.db import models

from usuarios.models import Usuarios

class MetodosDePago(models.Model):
    #Modelo de la tabla MetodosDePago para la base de datos
    id_metodoDePago=models.AutoField(primary_key=True, unique=True)
    numeroTarjeta=models.CharField(max_length=18)
    fechaEx = models.CharField(max_length=5)
    id_usuario=models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    
    #informacion principal de la tabla MetodosDePago
    class Meta:
        db_table = 'MetodosDePago'
        verbose_name ='metodo de pago'
        verbose_name_plural ='metodos de pago'

    def __str__(self) -> str:
        return self.numeroTarjeta
    

