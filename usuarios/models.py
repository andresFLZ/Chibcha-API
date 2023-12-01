from django.db import models

optionsTU = [
    [1, 'cliente'],
    [2, 'distribuidor']
]

class Pais (models.Model):
    #Modelo de la tabla País para la base de datos
    id_pais=models.AutoField(unique=True,primary_key=True)
    nombrePais=models.CharField(max_length=20, blank=False, verbose_name='Nombre del pais')

    #Información principal de la tabla
    class Meta:
        db_table = 'Pais'
        verbose_name = 'pais'
        verbose_name_plural = 'paises'

    def __str__(self):
        return self.nombrePais

class Paquetes(models.Model):
    #Modelo de la tabla Paquetes para la base de datos
    id_paquete=models.AutoField(primary_key=True,unique=True)
    nombrePaquete=models.CharField(max_length=20,unique=True, verbose_name='Nombre del paquete')
    cantDominios=models.IntegerField(verbose_name='Cantidad de dominios')
    gbsEspacio=models.IntegerField(verbose_name='Gigas Espacio', default=0)
    numCorreos=models.IntegerField(verbose_name='numero de correos corporativos', default=0)
    cantBasesDatos=models.IntegerField(verbose_name='cantidad de bases de datos', default=0)
    certificadoSSL=models.CharField(max_length=200, verbose_name='certificado SSL', default="")
    costoBase=models.IntegerField(verbose_name='costo mensual por plan', default=0)
    
    #Información principal de la tabla
    class Meta:
        db_table = 'Paquetes'
        verbose_name = 'paquete'
        verbose_name_plural = 'paquetes'

    def __str__(self):
        return self.nombrePaquete
    
class planPago(models.Model):
    id_planPago=models.AutoField(primary_key=True,unique=True)
    intervalos=models.CharField(max_length=20,unique=True, verbose_name='Intervalos de pago')
    cantMeses=models.IntegerField(verbose_name='cantidad de meses por intervalo',default=1)
    discount_pct=models.IntegerField(verbose_name='Porcentaje descuento del precio base')
        
    #Información principal de la tabla
    class Meta:
        db_table = 'PlanPago'
        verbose_name = 'Plan de pago'
        verbose_name_plural = 'planes de pago'

    def __str__(self):
        return self.intervalos

class Usuarios(models.Model):
    #Modelo de la tabla Usuarios para la base de datos
    id_usuario=models.AutoField(primary_key=True,unique=True)
    nombre=models.CharField(max_length=15)
    correo=models.CharField(max_length=40)
    contrase=models.CharField(max_length=15, verbose_name='contraseña')
    telefono=models.CharField(max_length=15,blank=True)
    tipo=models.IntegerField(choices=optionsTU, default=1)
    id_planPago=models.ForeignKey(planPago, on_delete=models.CASCADE, blank=True, null=True)
    metodoPago=models.BooleanField(default=False, verbose_name='método de pago')
    id_paquete=models.ForeignKey(Paquetes, on_delete=models.CASCADE, blank=True, null=True)
    id_pais=models.ForeignKey(Pais, on_delete=models.CASCADE, verbose_name='pais')

    #Información principal de la tabla
    class Meta:
        db_table = 'Usuarios'
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

    def __str__(self):
        return self.nombre