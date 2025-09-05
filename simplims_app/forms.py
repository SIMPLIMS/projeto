from django import forms

from .models import Matriz, Empresa, Parametro, Servico

class MatrizForm(forms.ModelForm):

    class Meta:
        model = Matriz
        fields = [
            'descricao',
        ]

class EmpresaForm(forms.ModelForm):

    class Meta:
        model = Empresa
        fields = [
            'apelido',
        ]

class ParametroForm(forms.ModelForm):

    class Meta:
        model = Parametro
        fields = [
            'descricao',
            'unidade_medida'
        ]

class ServicoForm(forms.ModelForm):

    class Meta:
        model = Servico
        fields = [
            'descricao',
            'matriz'
        ]

        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 1, 'placeholder': 'Descreva o serviço'}),
            'matriz': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'descricao': 'Descrição do Serviço',
            'matriz': 'Matriz',
        }

