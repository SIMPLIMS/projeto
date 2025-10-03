"""
Tudo o que é relativo às views de VisitaTecnica ficam aqui
"""

from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from datetime import date, timedelta
from django.utils import timezone

from ..forms import VisitaTecnicaForm
from ..models import VisitaTecnica
from .mixins import DeleteRecordMixin
from ..models import VisitaTecnica


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



class AgendaDiaView(ListView):
    model = VisitaTecnica
    template_name = "simplims_app/visita_tecnica/agenda.html"
    #context_object_name = "visitas"

    def get_queryset(self):
        """
        Filtra visitas pela data da URL ou pelo dia corrente
        """
        ano = self.kwargs.get("ano")
        mes = self.kwargs.get("mes")
        dia = self.kwargs.get("dia")

        if ano and mes and dia:
            data = date(int(ano), int(mes), int(dia))
        else:
            data = timezone.localdate()

        self.data = data  # guarda no objeto da view pra usar no contexto

        return VisitaTecnica.objects.filter(
            data_visita=data
        ).order_by("hora_visita")

    def get_context_data(self, **kwargs):
        """
        Adiciona data, anterior e próximo dia no contexto
        """
        contexto = super().get_context_data(**kwargs)
        contexto["data"] = self.data
        contexto["anterior"] = self.data - timedelta(days=1)
        contexto["proximo"] = self.data + timedelta(days=1)
        return contexto
