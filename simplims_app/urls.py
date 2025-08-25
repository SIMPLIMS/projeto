from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    # URLs da Matriz
    path('matrizes/', views.MatrizListView.as_view(), name='lista_matrizes'),
    path('matrizes/novo/', views.MatrizCreateView.as_view(), name='criar_matriz'),
    path('matrizes/<int:pk>/editar/', views.MatrizUpdateView.as_view(), name='editar_matriz'),
    path('matrizes/<int:pk>/excluir/', views.MatrizDeleteView.as_view(), name='excluir_matriz'),
]