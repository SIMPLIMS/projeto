"""
Tudo o que é relativo às views de OrdemServico ficam aqui
"""

from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from ..forms import OrdemServicoForm
from ..models import OrdemServico
from .mixins import DeleteRecordMixin


class OrdemServicoViewMixin:
    """
    Mixin para views de OrdemServico: define model, form e URL de sucesso.
    """

    model = OrdemServico
    form_class = OrdemServicoForm
    success_url = reverse_lazy("ordem_servico_listar")


class OrdemServicoListView(OrdemServicoViewMixin, ListView):
    # context_object_name = "ordem_servico"
    template_name = "simplims_app/ordem_servico/lista.html"


class OrdemServicoCreateView(OrdemServicoViewMixin, CreateView):
    template_name = "simplims_app/ordem_servico/formulario.html"


class OrdemServicoUpdateView(OrdemServicoViewMixin, UpdateView):
    template_name = "simplims_app/ordem_servico/formulario.html"


class OrdemServicoDeleteView(OrdemServicoViewMixin, DeleteRecordMixin, DeleteView):
    template_name = "simplims_app/ordem_servico/confirmar_exclusao.html"
