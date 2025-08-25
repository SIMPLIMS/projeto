from django.shortcuts import render
import calendar, locale
from calendar import HTMLCalendar
from datetime import datetime, timedelta
from .models import Matriz
from .mixins import MatrizViewMixin, DeleteRecordMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

def home(request, ano=datetime.now().year, mes=datetime.now().strftime('%B')):
    nome = "Andrimarciely"
    mes = mes.capitalize()

    # converte o nome do mês em número correspondente
   # numero_mes = list(calendar.month_name).index(mes)
   # numero_mes = int(numero_mes)

    # Create a calendar
  #  cal = HTMLCalendar().formatmonth(ano, numero_mes, withyear = True)

    # Get current year
    agora = datetime.now()
    mes = agora.strftime('%B')
    ano_corrente = agora.year

    # Get current time
    horario = agora.strftime('%H:%M')

    return render(request,'home.html',{
        "nome": nome,
        "ano": ano,
        "mes": mes,
#       "numero_mes": numero_mes,
#       "cal": cal,
        "ano_corrente": ano_corrente,
        "horario": horario,
        })

class MatrizListView(MatrizViewMixin, ListView):
    template_name = "simplims_app/matrizes/lista.html"
    context_object_name = "matriz"

class MatrizCreateView(MatrizViewMixin, CreateView):
    template_name = "simplims_app/matrizes/formulario.html"

class MatrizUpdateView(MatrizViewMixin, UpdateView):
    template_name = "simplims_app/matriz/formulario.html"

class MatrizDeleteView(MatrizViewMixin, DeleteRecordMixin, DeleteView):
    template_name = "simplims_app/matriz/confirmar_exclusao.html"