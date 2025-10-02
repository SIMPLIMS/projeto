"""
Tudo o que é relativo às views de VisitaTecnica ficam aqui
"""

from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from ..forms import VisitaTecnicaForm
from ..models import VisitaTecnica
from .mixins import DeleteRecordMixin


class VisitaTecnicaViewMixin:
    """
    Mixin para views de VisitaTecnica: define model, form e URL de sucesso.
    """

    model = VisitaTecnica
    form_class = VisitaTecnicaForm
    success_url = reverse_lazy("visita_tecnica_listar")


class VisitaTecnicaListView(VisitaTecnicaViewMixin, ListView):
    # context_object_name = "visita_tecnica"
    template_name = "simplims_app/visita_tecnica/lista.html"


class VisitaTecnicaCreateView(VisitaTecnicaViewMixin, CreateView):
    template_name = "simplims_app/visita_tecnica/formulario.html"


class VisitaTecnicaUpdateView(VisitaTecnicaViewMixin, UpdateView):
    template_name = "simplims_app/visita_tecnica/formulario.html"


class VisitaTecnicaDeleteView(VisitaTecnicaViewMixin, DeleteRecordMixin, DeleteView):
    template_name = "simplims_app/visita_tecnica/confirmar_exclusao.html"
