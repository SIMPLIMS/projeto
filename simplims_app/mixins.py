from django.urls import reverse_lazy
from .models import Matriz
from .forms import MatrizForm

class MatrizViewMixin:
    """
    Mixins para views de Matriz: define model, form e URL de sucesso.
    """
    model = Matriz
    form_class = MatrizForm
    success_url = reverse_lazy("lista_matrizes")