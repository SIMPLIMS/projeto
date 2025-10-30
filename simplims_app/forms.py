from django import forms

from .models import (
    Empresa,
    Matriz,
    OrdemServico,
    CategoriaParametro,
    TipoParametro,
    Parametro,
    Servico,
    Legislacao,
    VisitaTecnica,
)


class MatrizForm(forms.ModelForm):

    class Meta:
        model = Matriz
        fields = [
            "descricao",
        ]


class EmpresaForm(forms.ModelForm):

    class Meta:
        model = Empresa
        fields = [
            "apelido",
            "razao_social",
            "endereco",
            "telefone",
            "cnpj",
            "tipo_empresa",
            "email",
            "responsavel_tecnico",
        ]


class CategoriaParametroForm(forms.ModelForm):
    class Meta:
        model = CategoriaParametro
        fields = [
            "descricao",
        ]


class TipoParametroForm(forms.ModelForm):
    class Meta:
        model = TipoParametro
        fields = [
            "descricao",
        ]


class ParametroForm(forms.ModelForm):

    class Meta:
        model = Parametro
        fields = [
            "descricao",
            "unidade_medida",
            "categoria_parametro",
            "tipo_parametro",
        ]
        labels = {
            "descricao": "Descrição",
            "unidade_medida": "Unidade de Medida",
            "categoria_parametro": "Categoria",
            "tipo_parametro": "Tipo",
        }


class ServicoForm(forms.ModelForm):

    class Meta:
        model = Servico
        fields = ["descricao", "matriz"]

        widgets = {
            "descricao": forms.Textarea(
                attrs={"rows": 1, "placeholder": "Descreva o serviço"}
            ),
            "matriz": forms.Select(attrs={"class": "form-select"}),
        }
        labels = {
            "descricao": "Descrição do Serviço",
            "matriz": "Matriz",
        }


class OrdemServicoForm(forms.ModelForm):

    servicos = forms.ModelMultipleChoiceField(
        label="Serviços",
        help_text=
            "Selecione um ou mais serviços"
        ,
        queryset=Servico.objects.all(),
        required=True,
    )

    class Meta:
        model = OrdemServico
        fields = [
            "empresa",
            "servicos",
            "observacoes",
        ]

        widgets = {
            "empresa": forms.Select(attrs={"class": "form-control"}),
            "observacoes": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }


class LegislacaoForm(forms.ModelForm):

    class Meta:
        model = Legislacao
        fields = [
            "parametro",
            "valor_maximo",
            "observacao",
        ]

        widgets = {
            "parametro": forms.Select(attrs={"class": "form-control"}),
        }


class VisitaTecnicaForm(forms.ModelForm):
    class Meta:
        model = VisitaTecnica
        fields = "__all__"
        fields = [
            "ordem_servico",
            "data_visita",
            "hora_visita",
            "local",
            "responsavel",
            "observacoes",
            "status",
        ]
        widgets = {
            "data_visita": forms.DateInput(attrs={"type": "date"}),
            "hora_visita": forms.TimeInput(attrs={"type": "time"}),
            "observacoes": forms.Textarea(attrs={"rows": 3}),
            "status": forms.Select(),
        }
