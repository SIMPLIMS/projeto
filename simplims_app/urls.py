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
]
