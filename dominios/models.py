from distribuidores.models import Distribuidor
from metodosDePago.models import MetodosDePago
from usuarios.models import Usuarios
from metodosDePago.models import MetodosDePago
from django.db import models

class Dominios(models.Model):
    #Modelo de la tabla Dominios para la base de datos
    id_dom=models.AutoField(unique=True,primary_key=True)
    nombre_dom=models.CharField(max_length=25,unique=True, verbose_name='Nombre del dominio')
    paginaWeb=models.BooleanField(default=False, verbose_name='Página web')
    id_usuario=models.ForeignKey(Usuarios, on_delete=models.CASCADE, verbose_name='usuario', blank=True, null=True)
    id_distri=models.ForeignKey(Distribuidor, on_delete=models.CASCADE, verbose_name='Distribuidor', blank=True, null=True)
    solicitud=models.BooleanField(verbose_name="cumplimiento solicitud de migrado", default=False)
    repo=models.URLField(max_length = 200,default="")  

    #Información principal de la tabla
    class Meta:
        db_table = 'Dominios'
        verbose_name = 'dominios'
        verbose_name_plural = 'dominio'

    def __str__(self):
        return self.nombre_dom

class tipoHosting(models.Model):
    id_hosting=models.AutoField(unique=True,primary_key=True)
    nombreHosting=models.CharField(max_length=20, verbose_name='nombre del tipo de hosting')
    desc=models.CharField(max_length=200, verbose_name='descripcion hosting')
    class Meta:
            db_table = 'tipoHosting'
            verbose_name = 'tipo de hosting'
            verbose_name_plural = 'tipos de hosting'

    def __str__(self):
        return self.extension

class facturas(models.Model):
    #Modelo de la tabla MetodosDePago para la base de datos
    id_factura=models.AutoField(primary_key=True, unique=True)
    id_metodoDePago=models.ForeignKey(MetodosDePago, on_delete=models.CASCADE)
    d_dom=models.ForeignKey(Dominios, on_delete=models.CASCADE)
    
    #informacion principal de la tabla MetodosDePago
    class Meta:
        db_table = 'Facturas'
        verbose_name ='factura'
        verbose_name_plural ='mfacturas'

    def __str__(self) -> str:
        return self.id_factura