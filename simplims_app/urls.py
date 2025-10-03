from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # URLs da Matriz
    path("matriz/", views.MatrizListView.as_view(), name="matriz_listar"),
    path("matriz/novo/", views.MatrizCreateView.as_view(), name="matriz_criar"),
    path(
        "matriz/<int:pk>/editar/",
        views.MatrizUpdateView.as_view(),
        name="matriz_editar",
    ),
    path(
        "matriz/<int:pk>/excluir/",
        views.MatrizDeleteView.as_view(),
        name="matriz_excluir",
    ),
    # URLs da Empresa
    path("empresa/", views.EmpresaListView.as_view(), name="empresa_listar"),
    path("empresa/novo/", views.EmpresaCreateView.as_view(), name="empresa_criar"),
    path(
        "empresa/<int:pk>/editar/",
        views.EmpresaUpdateView.as_view(),
        name="empresa_editar",
    ),
    path(
        "empresa/<int:pk>/excluir/",
        views.EmpresaDeleteView.as_view(),
        name="empresa_excluir",
    ),
    # URLs de TipoParametro
    path(
        "tipo_parametro/",
        views.TipoParametroListView.as_view(),
        name="tipo_parametro_listar",
    ),
    path(
        "tipo_parametro/novo/",
        views.TipoParametroCreateView.as_view(),
        name="tipo_parametro_criar",
    ),
    path(
        "tipo_parametro/<int:pk>/editar/",
        views.TipoParametroUpdateView.as_view(),
        name="tipo_parametro_editar",
    ),
    path(
        "tipo_parametro/<int:pk>/excluir/",
        views.TipoParametroDeleteView.as_view(),
        name="tipo_parametro_excluir",
    ),
    # URLs de CategoriaParametro
    path(
        "categoria_parametro/",
        views.CategoriaParametroListView.as_view(),
        name="categoria_parametro_listar",
    ),
    path(
        "categoria_parametro/novo/",
        views.CategoriaParametroCreateView.as_view(),
        name="categoria_parametro_criar",
    ),
    path(
        "categoria_parametro/<int:pk>/editar/",
        views.CategoriaParametroUpdateView.as_view(),
        name="categoria_parametro_editar",
    ),
    path(
        "categoria_parametro/<int:pk>/excluir/",
        views.CategoriaParametroDeleteView.as_view(),
        name="categoria_parametro_excluir",
    ),
    # URLs de Parametros
    path("parametro/", views.ParametroListView.as_view(), name="parametro_listar"),
    path(
        "parametro/novo/", views.ParametroCreateView.as_view(), name="parametro_criar"
    ),
    path(
        "parametro/<int:pk>/editar/",
        views.ParametroUpdateView.as_view(),
        name="parametro_editar",
    ),
    path(
        "parametro/<int:pk>/excluir/",
        views.ParametroDeleteView.as_view(),
        name="parametro_excluir",
    ),
    # URLs de Servicos
    path("servico/", views.ServicoListView.as_view(), name="servico_listar"),
    path("servico/novo/", views.ServicoCreateView.as_view(), name="servico_criar"),
    path(
        "servico/<int:pk>/editar/",
        views.ServicoUpdateView.as_view(),
        name="servico_editar",
    ),
    path(
        "servico/<int:pk>/excluir/",
        views.ServicoDeleteView.as_view(),
        name="servico_excluir",
    ),
    # URLs de Ordem de Servicos
    path(
        "ordem_servico/",
        views.OrdemServicoListView.as_view(),
        name="ordem_servico_listar",
    ),
    path(
        "ordem_servico/novo/",
        views.OrdemServicoCreateView.as_view(),
        name="ordem_servico_criar",
    ),
    path(
        "ordem_servico/<int:pk>/editar/",
        views.OrdemServicoUpdateView.as_view(),
        name="ordem_servico_editar",
    ),
    path(
        "ordem_servico/<int:pk>/excluir/",
        views.OrdemServicoDeleteView.as_view(),
        name="ordem_servico_excluir",
    ),
    # URLs de Legislação
    path(
        "legislacao/",
        views.LegislacaoListView.as_view(),
        name="legislacao_listar",
    ),
    path(
        "legislacao/novo/",
        views.LegislacaoCreateView.as_view(),
        name="legislacao_criar",
    ),
    path(
        "legislacao/<int:pk>/editar/",
        views.LegislacaoUpdateView.as_view(),
        name="legislacao_editar",
    ),
    path(
        "legislacao/<int:pk>/excluir/",
        views.LegislacaoDeleteView.as_view(),
        name="legislacao_excluir",
    ),

# URLs de VisitaTecnica
    path(
        "visita_tecnica/",
        views.VisitaTecnicaListView.as_view(),
        name="visita_tecnica_listar",
    ),
    path(
        "visita_tecnica/novo/",
        views.VisitaTecnicaCreateView.as_view(),
        name="visita_tecnica_criar",
    ),
    path(
        "visita_tecnica/<int:pk>/editar/",
        views.VisitaTecnicaUpdateView.as_view(),
        name="visita_tecnica_editar",
    ),
    path(
        "visita_tecnica/<int:pk>/excluir/",
        views.VisitaTecnicaDeleteView.as_view(),
        name="visita_tecnica_excluir",
    ),

    # Agenda
    path("visita_tecnica/agenda/", AgendaDiaView.as_view(), name="visita_tecnica_agenda"),
    path("visita_tecnica/agenda/<int:ano>/<int:mes>/<int:dia>/", AgendaDiaView.as_view(), name="visita_tecnica_agenda_dia"),
]

