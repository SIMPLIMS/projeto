from django.db import models

class Legislacao(models.Model):
    parametro = models.ForeignKey("Parametro", on_delete=models.CASCADE)
    valor_maximo = models.FloatField(null=True, blank=True)
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.parametro.descricao}"
