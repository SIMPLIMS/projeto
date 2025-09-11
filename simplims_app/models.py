from django.db import models

# Create your models here.


class Matriz(models.Model):
    descricao = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Matriz"
        verbose_name_plural = "Matrizes"


class Empresa(models.Model):
    TIPOS = [
        ("CONSULTORIA", "Consultoria Ambiental"),
        ("CLIENTE", "Cliente"),
        ("FORNECEDOR", "Fornecedor"),
    ]

    apelido = models.CharField(
        help_text="Apelido ou abreviação", max_length=200, verbose_name="Apelido"
    )

    razao_social = models.CharField(
        help_text="Razão social da empresa",
        max_length=200,
        verbose_name="Razão Social",
    )

    endereco = models.CharField(
        help_text="Endereço completo", max_length=200, verbose_name="Endereço"
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

    tipo_empresa = models.CharField(
        max_length=20,
        choices=TIPOS,
        verbose_name="Tipo de Empresa",
    )

    email = models.EmailField(
        blank=True,
        null=True,
        help_text="Endereço de e-mail",
        verbose_name="E-mail",
    )

    responsavel_tecnico = models.CharField(
        max_length=80,
        blank=True,
        null=True,
        help_text="Responsável técnico (apenas para clientes)",
        verbose_name="Responsável Técnico",
    )

    def __str__(self):
        return self.apelido

class CategoriaParametro(models.Model):
    descricao = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.descricao

class TipoParametro(models.Model):
    descricao = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.descricao

class Parametro(models.Model):
    descricao = models.CharField(max_length=100, unique=True)

    unidade_medida = models.CharField(
        help_text="Unidade de medida",
        max_length=10,
        verbose_name="Unidade",
    )

    tipo_parametro = models.ForeignKey(
        "TipoParametro",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
     )

    categoria_parametro = models.ForeignKey(
        "CategoriaParametro",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
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
    empresa = models.ForeignKey(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa Cliente"
    )
    servico = models.ForeignKey(
        Servico, on_delete=models.CASCADE, verbose_name="Serviço Contratado"
    )
    quantidade_amostras = models.PositiveIntegerField(
        verbose_name="Quantidade de Amostras"
    )
    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações")
    matriz = models.ForeignKey(
        "Matriz",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"OS {self.numero} - {self.empresa.nome}"

    class Meta:
        verbose_name = "Ordem de Serviço"
        verbose_name_plural = "Ordens de Serviço"


class Amostra(models.Model):
    ordem_servico = models.ForeignKey(
        "OrdemServico",
        on_delete=models.CASCADE,
        related_name="amostras",
        verbose_name="Ordem de Serviço",
    )

    servico = models.ForeignKey(
        "Servico", on_delete=models.CASCADE, verbose_name="Serviço Contratado"
    )

    volume = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Volume", null=True, blank=True
    )

    horario_coleta = models.TimeField(verbose_name="Horário da Coleta")
    local_coleta = models.CharField(max_length=200, verbose_name="Local da Coleta")

    ph = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="pH", null=True, blank=True
    )
    temperatura = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Temperatura (°C)",
        null=True,
        blank=True,
    )
    solidos_sedimentaveis = models.DecimalField(
        max_digits=7,
        decimal_places=3,
        verbose_name="Sólidos Sedimentáveis (mL/L)",
        null=True,
        blank=True,
    )
    materiais_flutuantes = models.BooleanField(
        default=False, verbose_name="Materiais Flutuantes"
    )

    data_registro = models.DateTimeField(
        auto_now_add=True, verbose_name="Data de Registro"
    )

    def __str__(self):
        return f"Amostra {self.id}"


class ResultadoAmostraParametro(models.Model):
    amostra = models.ForeignKey(
        Amostra,
        on_delete=models.CASCADE,
        related_name="resultados",
        verbose_name="Amostra",
    )
    parametro = models.ForeignKey(
        "Parametro", on_delete=models.CASCADE, verbose_name="Parâmetro"
    )
    resultado = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Resultado"
    )
    unidade = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="Unidade"
    )
    data_analise = models.DateField(
        null=True, blank=True, verbose_name="Data da Análise"
    )

    class Meta:
        verbose_name = "Resultado de Parâmetro da Amostra"
        verbose_name_plural = "Resultados de Parâmetros das Amostras"
        unique_together = ("amostra", "parametro")  # evita duplicidade

    def __str__(self):
        return f"{self.parametro.descricao} - Amostra {self.amostra.id}: {self.resultado or 'pendente'}"


class Legislacao(models.Model):
    parametro = models.ForeignKey("Parametro", on_delete=models.CASCADE)
    valor_minimo = models.FloatField(null=True, blank=True)
    valor_maximo = models.FloatField(null=True, blank=True)
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.parametro.descricao}"
