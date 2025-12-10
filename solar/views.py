from django.shortcuts import render, redirect, get_object_or_404
from solar.models import PessoaFisica, PessoaJuridica
from django.urls import reverse
from django.http import HttpResponse,JsonResponse
from solar.models import Produto
from solar.forms import ProdutoForm
from django.contrib import messages

def home(request):
    return render(request,'home.html')

def gerenciamento(request):
    fisicas = PessoaFisica.objects.all()
    juridicas = PessoaJuridica.objects.all()
    
    return render(request, 'gerenciar_usuarios.html', {
        'fisicas': fisicas,
        'juridicas': juridicas
         })

         
def PessoaFisicaInsert(request):
   if request.method == 'POST':
    # Pegando os dados do formulário HTML pelo name=""
      cpf = request.POST.get('cpf')
      nome = request.POST.get('nome')
      dataNascimento = request.POST.get('data_nascimento')
      rg = request.POST.get('rg')
      email = request.POST.get('email')
      telefone1 = request.POST.get('telefone_principal')
      telefone2 = request.POST.get('telefone_secundario')
      cep = request.POST.get('cep')
      Logadouro = request.POST.get('logradouro')
      Numero = request.POST.get('numero')
      Complemento = request.POST.get('complemento')
      Bairro = request.POST.get('bairro')
      Cidade = request.POST.get('cidade')
      Estado = request.POST.get('estado')
      Pais = request.POST.get('pais')
   # Cria e salva no banco
      PessoaFisica.objects.create(
          cpf = cpf,
          nome_completo = nome,
          data_nascimento = dataNascimento,
          rg = rg,
          email = email,
          telefone_principal = telefone1,
          telefone_secundario = telefone2,
          cep = cep,
          logradouro = Logadouro,
          numero = Numero,
          complemento = Complemento,
          bairro = Bairro,
          cidade = Cidade,
          estado = Estado,
          pais =  Pais                                                                                                                                                    
        )

    # Redireciona após o cadastro
      return redirect(reverse('home'))
                                                                                                                                                                                                        
 # Se for GET, apenas mostra o formulário
   return render(request, 'pessoaFisicaForm.html')
                                                                                                                                                                                                                


def PessoaJuridicaInsert(request):
     if request.method == 'POST':
    # Pegando os dados do formulário HTML pelo name=""
      cnpj = request.POST.get('cnpj')
      razaoSocial = request.POST.get('razao_social')
      nome_fantasia = request.POST.get('nome_fantasia')
      abertura = request.POST.get('data_abertura')
      inscricaoEstadual= request.POST.get('inscricao_estadual')
      email = request.POST.get('email')
      telefone1 = request.POST.get('telefone_principal')
      telefone2 = request.POST.get('telefone_secundario')
      site = request.POST.get('site')
      cep = request.POST.get('cep')
      Logadouro = request.POST.get('logradouro')
      Numero = request.POST.get('numero')
      Complemento = request.POST.get('complemento')
      Bairro = request.POST.get('bairro')
      Cidade = request.POST.get('cidade')
      Estado = request.POST.get('estado')
      Pais = request.POST.get('pais')
   # Cria e salva no banco
      PessoaFisica.objects.create(
          cnpj = cnpj,
          razao_social = razaoSocial,
          nome_fantasia = nome_fantasia,
          data_abertura = abertura,
          inscricao_estadual = inscricaoEstadual,
          email = email,
          telefone_principal = telefone1,
          telefone_secundario = telefone2,
          site = site,
          cep = cep,
          logradouro = Logadouro,
          numero = Numero,
          complemento = Complemento,
          bairro = Bairro,
          cidade = Cidade,
          estado = Estado,
          pais =  Pais                                                                                                                                                    
        )

      return redirect(reverse('home'))
                                                                                                                                                                                                        
     return render(request, 'pessoaJuridicaForm.html')


def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto cadastrado com sucesso!')
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    
    return render(request, 'cadastrar_produtos.html', {'form': form})

def lista_produtos(request):
    produtos = Produto.objects.all().order_by('nome')
    return render(request, 'listar_produtos.html', {'produtos': produtos})


def Listar_por_categoria(request):
    nome_categoria= request.GET.get('categoria')  
    produtos = Produto.objects.filter(categoria= nome_categoria)
    match nome_categoria:
        case "MODULOS":
           return render(request, 'listar_produtos.html',{
              'nome_categoria': nome_categoria, 
              'produtos': produtos })
           
        case "INVERSORES":
          return render(request, 'listar_produtos.html', {
              'nome_categoria': nome_categoria,
              'produtos': produtos})
          
        case "COMPONENTES_ELETRONICOS":
           return render(request, 'listar_produtos.html', {
              'nome_categoria': nome_categoria,
              'produtos': produtos })
           
        case "ESTRUTURAS_GALVANIZADAS":
           return render(request, 'listar_produtos.html', {
             'nome_categoria': nome_categoria,
             'produtos': produtos })
           
        case "PARAFUSOS":
           return render(request, 'listar_produtos.html', {
             'nome_categoria': nome_categoria,
             'produtos': produtos})
           
        case "CABOS":
            return render(request, 'listar_produtos.html', {
             'nome_categoria': nome_categoria,
             'produtos': produtos})

        case "BATERIAS":
           return render(request, 'listar_produtos.html', {
             'nome_categoria': nome_categoria,
             'produtos': produtos})
       
def adicionar_ao_carrinho(request, produto_id):
    """Adiciona produto ao carrinho via sessÃ£o"""
    if request.method == 'POST':
        quantidade = int(request.POST.get('quantidade', 1))
        
        # ObtÃ©m o produto
        produto = get_object_or_404(Produto, id=produto_id)
        
        # Inicializa o carrinho na sessÃ£o se nÃ£o existir
        if 'carrinho' not in request.session:
            request.session['carrinho'] = {}
        
        carrinho = request.session['carrinho']
        
        # Converte produto_id para string (chave de dicionÃ¡rio)
        produto_id_str = str(produto_id)
        
        # Se o produto jÃ¡ estÃ¡ no carrinho, incrementa a quantidade
        if produto_id_str in carrinho:
            carrinho[produto_id_str]['quantidade'] += quantidade
        else:
            # Adiciona novo produto ao carrinho
            carrinho[produto_id_str] = {
                'id': produto.id,
                'nome': produto.nome,
                'preco': float(produto.preco),  # Convertendo para float para JSON
                'quantidade': quantidade,
                'imagem': produto.imagem.url if produto.imagem else '',
                'codigo': produto.codigo,
            }
        
        # Salva a sessÃ£o
        request.session.modified = True
        messages.success(request, f'{quantidade} x {produto.nome} adicionado ao carrinho!')
        
        return redirect('listar_produtos')
    
    return redirect('listar_produtos')


def ver_carrinho(request):
    """Exibe o carrinho de compras"""
    carrinho = request.session.get('carrinho', {})
    
    # Calcula totais
    total_itens = 0
    total_preco = 0
    
    for item in carrinho.values():
        total_itens += item['quantidade']
        total_preco += item['quantidade'] * item['preco']
    
    context = {
        'carrinho': carrinho,
        'total_itens': total_itens,
        'total_preco': total_preco,
    }
    
    return render(request, 'carrinho.html', context)
