from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar_produto/', views.cadastrar_produto, name='cadastrar_produto'),
    path('iniciar_venda/', views.iniciar_venda, name='iniciar_venda'),
    path('inserir_produto_venda/<int:venda_id>/', views.inserir_produto_venda, name='inserir_produto_venda'),
    path('fechar_venda/<int:venda_id>/', views.fechar_venda, name='fechar_venda'),
    path('listar_vendas/', views.listar_vendas, name='listar_vendas'),
    path('cadastrar_vendedor/', views.cadastrar_vendedor, name='cadastrar_vendedor'),  # Nova rota
]
