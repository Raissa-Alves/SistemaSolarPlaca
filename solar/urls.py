from django.urls import path
from solar import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('Categoria/', views.Listar_por_categoria, name='Categoria'),
    path('lista_produtos', views.lista_produtos, name='lista_produtos'),
    path('cadastrar_produto/', views.cadastrar_produto, name='cadastrar_produto'),
    path('gerenciamento/', views.gerenciamento, name='gerenciamento'),
    path('pf_Cadastro/',views.PessoaFisicaInsert, name='pf_Cadastro'),
    path('pj_Cadastro/',views.PessoaJuridicaInsert,name='pj_Cadastro'),
]