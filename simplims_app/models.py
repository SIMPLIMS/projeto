from django.db import models

# Create your models here.

class Matriz(models.Model):
    descricao = models.CharField(max_length=100, unique = True)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Matriz"
        verbose_name_plural = "Matrizes"
