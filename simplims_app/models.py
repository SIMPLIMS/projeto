from django.db import models

# Create your models here.

class Matriz(models.Model):
    descricao = models.CharField(max_length=100, unique = True)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Matriz"
        verbose_name_plural = "Matrizes"


class Empresa(models.Model):
    TIPOS = [
        ("CONSULTORIA", "Consultoria Ambiental"),
        ("CLIENTE", "Cliente"),
        ("FORNECEDOR","Fornecedor" ),
    ]

    apelido = models.CharField(
        help_text="Apelido ou abreviação",
        max_length=200,
        verbose_name="Apelido"
    )

    razao_social = models.CharField(
        help_text="Razão social da empresa",
        max_length=200,
        verbose_name="Razão Social",
    )

    endereco = models.CharField(
        help_text="Endereço completo",
        max_length=200,
        verbose_name="Endereço"
    )

    telefone = models.CharField(
        help_text="Telefone para contato",
        max_length=15,
        verbose_name="Telefone/Fax",
    )

    cnpj = models.CharField(
        help_text="CNPJ",
        max_length=20,
        verbose_name="CNPJ",
    )

    tipo_empresa= models.CharField(
        max_length= 20,
        choices = TIPOS,
        verbose_name="Tipo de Empresa",
    )

    email = models.EmailField(
        blank=True,
        null=True,
        help_text= "Endereço de e-mail",
        verbose_name="E-mail",
    )

    responsavel_tecnico= models.CharField(
        max_length=80,
        blank=True,
        null=True,
        help_text="Responsável técnico (apenas para clientes)",
        verbose_name="Responsável Técnico",
    )

    def __str__(self):
        return self.apelido


class Parametro(models.Model):
    descricao = models.CharField(max_length=100, unique = True)

    unidade_medida = models.CharField(
        help_text="Unidade de medida",
        max_length=10,
        verbose_name="Unidade",
    )

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Parametro"


class Servico(models.Model):
    descricao = models.CharField(max_length=100, unique=True)

    matriz = models.ForeignKey(
        "Matriz",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Serviço"

class OrdemServico(models.Model):
    data_emissao = models.DateField(auto_now_add=True, verbose_name="Data de Emissão")
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name="Empresa Cliente")
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, verbose_name="Serviço Contratado")
    quantidade_amostras = models.PositiveIntegerField(verbose_name="Quantidade de Amostras")
    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações")
    matriz = models.ForeignKey(
        "Matriz",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Ordem de Serviço"
        verbose_name_plural = "Ordens de Serviço"