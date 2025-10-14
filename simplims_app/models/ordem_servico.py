from django.db import models

from . import Matriz
from .empresa import Empresa
from .servico import Servico


class OrdemServico(models.Model):
    data_emissao = models.DateField(auto_now_add=True, verbose_name="Data de Emissão")
    empresa = models.ForeignKey(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa Cliente"
    )
    quantidade_amostras = models.PositiveIntegerField(
        verbose_name="Quantidade de Amostras"
    )
    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações")
    servicos = models.ManyToManyField(
        Servico,
        blank=False,
        help_text="Selecione os serviços desta OS",
        verbose_name="Serviços contratados",
    )

    def __str__(self) -> str:
        return f"OS {self.numero} - {self.empresa.nome}"

    class Meta:
        verbose_name = "Ordem de Serviço"
        verbose_name_plural = "Ordens de Serviço"
