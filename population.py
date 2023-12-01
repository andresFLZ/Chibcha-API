import os
import time
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE","api_webchibcha.settings")

django.setup()

from usuarios.models import planPago,Paquetes

def generarPlanesPago():
    planPago.objects.create(
        id_planPago=5,
        intervalos='mensual',
        cantMeses=1,
        discount_pct=0
        
    )
    planPago.objects.create(
        id_planPago=6,
        intervalos='trimestral',
        cantMeses=3,
        discount_pct=6
        
    )
    planPago.objects.create(
        id_planPago=7,
        intervalos='semestral',
        cantMeses=6,
        discount_pct=10
        
    )
    planPago.objects.create(
        id_planPago=8,
        intervalos='anual',
        cantMeses=12,
        discount_pct=17
        
    )
def generarPlanes():
    Paquetes.objects.create(
        id_paquete=1,
        nombrePaquete='plata',
        cantDominios=10,
        gbsEspacio=10,
        numCorreos=10,
        cantBasesDatos=2,
        certificadoSSL='este es el certificado',
        costoBase=12400
               
    )
    
    Paquetes.objects.create(
        id_paquete=2,
        nombrePaquete='oro',
        cantDominios=20,
        gbsEspacio=20,
        numCorreos=20,
        cantBasesDatos=10,
        certificadoSSL='este es el certificado',
        costoBase=23100
               
    )
    
    Paquetes.objects.create(
        id_paquete=3,
        nombrePaquete='platino',
        cantDominios=200,
        gbsEspacio=60,
        numCorreos=150,
        cantBasesDatos=200,
        certificadoSSL='este es el certificado',
        costoBase=66700
               
    )
    
if __name__=="__main__":
    print('creando datos iniciales')
    generarPlanes()
    generarPlanesPago()
    print('datos correctamente inicializados')