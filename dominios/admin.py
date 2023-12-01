from django.contrib import admin
from .models import Dominios,tipoHosting,facturas

admin.site.register(Dominios)
admin.site.register(tipoHosting)
admin.site.register(facturas)