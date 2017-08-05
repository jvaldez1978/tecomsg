from django.contrib import admin
from almacen.models import Unidad, Material, Persona, Empresa

# Register your models here.
admin.site.register(Unidad)
admin.site.register(Material)
admin.site.register(Persona)
admin.site.register(Empresa)