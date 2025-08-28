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

    apelido = models.Charfield(
        help_text="Apelido ou abreviação",
        max_lenght=200,
        verbose_name="Apelido"
    )

    razao_social = models.CharField(
        help_text="Razão social da empresa",
        max_length=200,
        verbose_name="Razão Social",
    )

    endereco = models.CharField(
        help_text="Endereço completo",
        max_lenght=200,
        verbose_name="Endereço"
    )

    telefone = models.CharField(
        help_text="Telefone para contato",
        max_lenght=15,
        verbose_name="Telefone/Fax",
    )

    cnpj = models.CharField(
        help_text="CNPJ",
        max_lenght=20,
        vero
    )

    tipo_empresa= models.CharField(
        max_length= 20,
        choices = TIPOS,
        VERBOSE_NAME="Tipo de Empresa",
    )

    email = models.EmailField(
        blank=True,
        null=True,
        help_text= "Endereço de e-mail",
        verbose_name="E-mail",
    )

    responsavel_tecnico= models.CharFiel(
        max_lenght=80,
        blank=True,
        null=True,
        help_text="Responsável técnico (apenas para clientes)",
        verbose_name="Responsável Técnico",
    )

    def __str__(self):
        return f"{self.razao_social} ({self.apelido})"