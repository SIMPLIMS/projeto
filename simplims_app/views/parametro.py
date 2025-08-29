"""
Tudo o que é relativo às views de Parametro ficam aqui
"""
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from ..forms import ParametroForm
from ..models import Parametro
from .mixins import DeleteRecordMixin


class ParametroViewMixin:
    """
    Mixin para views de Parametro: define model, form e URL de sucesso.
    """

    model = Parametro
    form_class = ParametroForm
    success_url = reverse_lazy("parametro_listar")


class ParametroListView(ParametroViewMixin, ListView):
    # context_object_name = "parametro"
    template_name = "simplims_app/parametro/lista.html"


class ParametroCreateView(ParametroViewMixin, CreateView):
    template_name = "simplims_app/parametro/formulario.html"


class ParametroUpdateView(ParametroViewMixin, UpdateView):
    template_name = "simplims_app/parametro/formulario.html"


class ParametroDeleteView(ParametroViewMixin, DeleteRecordMixin, DeleteView):
    template_name = "simplims_app/parametro/confirmar_exclusao.html"
