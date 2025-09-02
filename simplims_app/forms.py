from django import forms

from .models import Matriz, Empresa, Parametro

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