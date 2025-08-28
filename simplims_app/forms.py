from django import forms

from .models import Matriz, Empresa

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