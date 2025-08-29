import calendar
import locale
from calendar import HTMLCalendar
from datetime import datetime, timedelta

from django.shortcuts import render

from .matriz import (
    MatrizCreateView,
    MatrizDeleteView,
    MatrizListView,
    MatrizUpdateView,
)

from .empresa import (
    EmpresaCreateView,
    EmpresaDeleteView,
    EmpresaListView,
    EmpresaUpdateView,
)

from .parametro import (
    ParametroCreateView,
    ParametroDeleteView,
    ParametroListView,
    ParametroUpdateView,
)

locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")


def home(request, ano=None, mes=None):
    nome = "Andrimarciely"

    data_corrente = datetime.now()

    if not ano:
        ano = data_corrente.year

    if not mes:
        mes = data_corrente.month

    data_do_calendario = datetime(ano, mes, 1)

    return render(
        request,
        "home.html",
        {
            "nome": nome,
            "data_corrente": data_corrente,
            "data_calendario": data_do_calendario,
        },
    )
