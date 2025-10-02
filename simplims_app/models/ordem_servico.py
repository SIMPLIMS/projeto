from django.db import models
from .empresa import Empresa
from .servico import Servico


class OrdemServico(models.Model):
    data_emissao = models.DateField(
        auto_now_add=True, verbose_name="Data de Emissão"
    )
    empresa = models.ForeignKey(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa Cliente"
    )
    servico = models.ForeignKey(
        Servico, on_delete=models.CASCADE, verbose_name="Serviço Contratado"
    )
    quantidade_amostras = models.PositiveIntegerField(
        verbose_name="Quantidade de Amostras"
    )
    observacoes = models.TextField(
        blank=True, null=True, verbose_name="Observações"
    )
    matriz = models.ForeignKey(
        "Matriz",
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"OS {self.id} - {self.empresa}"

    class Meta:
        verbose_name = "Ordem de Serviço"
        verbose_name_plural = "Ordens de Serviço"
