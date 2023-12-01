from django.db import models
from usuarios.models import Usuarios
from metodosDePago.models import MetodosDePago

class Categoria (models.Model):
    #Modelo de la tabla categoría para la base de datos
    id_Categoria=models.AutoField(unique=True,primary_key=True)
    nombreCategoria=models.CharField(max_length=20, verbose_name='nombre de categoría')
    comision_pct=models.DecimalField(max_digits=4, decimal_places=2, verbose_name='comisión')

    #Información principal de la tabla
    class Meta:
        db_table = 'Categoria'
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombreCategoria

class Distribuidor(models.Model):
    #Modelo de la tabla Distribuidor para la base de datos
    id_distri=models.AutoField(unique=True,primary_key=True)
    nombreDistr=models.CharField(max_length=20, verbose_name='Nombre del distribuidor')
    numeroDominios=models.IntegerField(default=0, verbose_name='Numero de dominios', blank=True, null=True)
    correo=models.CharField(max_length=40,unique=True, verbose_name='Correo corporativo', blank=True, null=True)
    solicitud=models.BooleanField(verbose_name="solicitud para ser distribuidor", default=True)
    id_categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoría')
    id_usuario=models.ForeignKey(Usuarios, on_delete=models.CASCADE, verbose_name='usuario', null=True)

    #Información principal de la tabla
    class Meta:
        db_table = 'Distribuidor'
        verbose_name = 'distribuidor'
        verbose_name_plural = 'distribuidores'

    def __str__(self):
        return self.nombreDistr
    
class PagoComisiones(models.Model):
    #Modelo de la tabla Distribuidor para la base de datos
    id_comision=models.AutoField(unique=True,primary_key=True)
    id_distri=models.ForeignKey(Distribuidor, on_delete=models.CASCADE, verbose_name='Distribuidor')
    ValorPagar=models.IntegerField(default=0, verbose_name='Valor a pagar', blank=True, null=True)
    pagado=models.BooleanField(verbose_name="Esta pagado", default=False)
    id_metodoDePago=models.ForeignKey(MetodosDePago, on_delete=models.CASCADE, verbose_name='Método de pago', blank=True, null=True)

    #Información principal de la tabla
    class Meta:
        db_table = 'Pagocomisiones'
        verbose_name = 'PagoComision'
        verbose_name_plural = 'PagoComisiones'

    def __str__(self):
        return self.id_comision


