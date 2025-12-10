from django.urls import path
from solar import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/',views.home,name='home'),

    path('carrinho/adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('carrinho/', views.ver_carrinho, name='ver_carrinho'),
    
    path('Categoria/', views.Listar_por_categoria, name='Categoria'),
    path('lista_produtos', views.lista_produtos, name='lista_produtos'),
    path('cadastrar_produto/', views.cadastrar_produto, name='cadastrar_produto'),
    path('gerenciamento/', views.gerenciamento, name='gerenciamento'),
    path('pf_Cadastro/',views.PessoaFisicaInsert, name='pf_Cadastro'),
    path('pj_Cadastro/',views.PessoaJuridicaInsert,name='pj_Cadastro'),
]
