from django.contrib import admin
from .models import Matriz, Empresa, Parametro, Servico

# Register your models here.
admin.site.register(Matriz)
admin.site.register(Empresa)
admin.site.register(Parametro)
admin.site.register(Servico)