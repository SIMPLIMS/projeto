from django.contrib import admin

from .models import (Amostra, Empresa, Legislacao, Matriz, OrdemServico,TipoParametro,
                     Parametro, ResultadoAmostraParametro, Servico)

# Register your models here.
admin.site.register(Matriz)
admin.site.register(Empresa)
admin.site.register(TipoParametro)
admin.site.register(Parametro)
admin.site.register(Servico)
admin.site.register(OrdemServico)
admin.site.register(Amostra)
admin.site.register(ResultadoAmostraParametro)
admin.site.register(Legislacao)
