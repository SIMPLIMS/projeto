from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    # URLs da Matriz
    path('matriz/', views.MatrizListView.as_view(), name='matriz_listar'),
    path('matriz/novo/', views.MatrizCreateView.as_view(), name='matriz_criar'),
    path('matriz/<int:pk>/editar/', views.MatrizUpdateView.as_view(), name='matriz_editar'),
    path('matriz/<int:pk>/excluir/', views.MatrizDeleteView.as_view(), name='matriz_excluir'),
]