from django.urls import reverse_lazy
from .models import Matriz
from .forms import MatrizForm
from django.urls import reverse_lazy

class MatrizViewMixin:
    """
    Mixin para views de Matriz: define model, form e URL de sucesso.
    """
    model = Matriz
    form_class = MatrizForm
    success_url = reverse_lazy("matriz_listar")


class DeleteRecordMixin:
    """
       Mixin para adicionar lógica extra em DeleteView (mensagens, logs, etc.)
    """
    def delete(self, request, *args, **kwargs):
        # Aqui você pode adicionar lógica comum, como log ou mensagens
        print(f"Registro será deletado: {self.object}")
        success_message = "Registro excluído com sucesso."
        return super().delete(request, *args, **kwargs)