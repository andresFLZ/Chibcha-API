from django.contrib import admin
from .models import Paquetes, Usuarios, Pais,planPago

admin.site.register(Paquetes)
admin.site.register(Usuarios)
admin.site.register(Pais)
admin.site.register(planPago)