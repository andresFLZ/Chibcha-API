from django.contrib import admin
from .models import Categoria, Distribuidor,PagoComisiones

admin.site.register(Categoria)
admin.site.register(Distribuidor)
admin.site.register(PagoComisiones)
