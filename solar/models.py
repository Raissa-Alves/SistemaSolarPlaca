from django.db import models
from django.core.files import File
from PIL import Image

class PessoaFisica(models.Model):
        cpf = models.CharField(max_length=14, unique=True)
        nome_completo = models.CharField(max_length=150)
        data_nascimento = models.DateField()
        rg = models.CharField(max_length=20)
        email = models.EmailField()
        telefone_principal = models.CharField(max_length=15)
        telefone_secundario = models.CharField(max_length=15, blank=True, null=True)
        cep = models.CharField(max_length=9)
        logradouro = models.CharField(max_length=150)
        numero = models.CharField(max_length=10)
        complemento = models.CharField(max_length=50, blank=True, null=True)
        bairro = models.CharField(max_length=80)
        cidade = models.CharField(max_length=100)
        estado = models.CharField(max_length=2)
        pais = models.CharField(max_length=50)

        def __str__(self):
          return f"{self.nome_completo} (CPF: {self.cpf})"
        

class PessoaJuridica(models.Model):
        cnpj = models.CharField(max_length=18, unique=True)
        razao_social = models.CharField(max_length=150)
        nome_fantasia = models.CharField(max_length=150, blank=True, null=True)
        data_abertura = models.DateField()
        inscricao_estadual = models.CharField(max_length=20)
        email = models.EmailField()
        telefone_principal = models.CharField(max_length=15)
        telefone_secundario = models.CharField(max_length=15, blank=True, null=True)
        site = models.URLField(blank=True, null=True)
        cep = models.CharField(max_length=9)
        logradouro = models.CharField(max_length=150)
        numero = models.CharField(max_length=10)
        complemento = models.CharField(max_length=50, blank=True, null=True)
        bairro = models.CharField(max_length=80)
        cidade = models.CharField(max_length=100)
        estado = models.CharField(max_length=2)
        pais = models.CharField(max_length=50)

        def __str__(self):
           return f"{self.razao_social} (CNPJ: {self.cnpj})"
        
        
 
from django.db import models

class Produto(models.Model):
    FORMA_PAGAMENTO_CHOICES = [
        ("PIX", "Pix"),
        ("CARTÃO", "Cartao")
    ]
    
    CATEGORIA_CHOICES = [
        ("MODULOS", "Módulos"),
        ("INVERSORES", "Inversores"),
        ("COMPONENTES_ELETRONICOS", "Componentes Eletrônicos"),
        ("ESTRUTURAS_GALVANIZADAS", "Estruturas Galvanizadas"),
        ("PARAFUSOS", "Parafusos"),
        ("CABOS", "Cabos"),
        ("BATERIAS", "Baterias"),
    ]
    codigo = models.IntegerField(unique=True, default=1)    
    nome = models.CharField(max_length=100, default='Novo Produto')
    imagem = models.ImageField(upload_to='uploads/', blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    Q_Estoque = models.IntegerField(default=0)
    Forma_Pagamento = models.CharField(
        max_length=20, 
        choices=FORMA_PAGAMENTO_CHOICES, 
        default='PIX'
    )
    categoria = models.CharField(
        max_length=30, 
        choices=CATEGORIA_CHOICES, 
        default='MODULOS'
    )
    descricao = models.TextField(default='Descrição do produto será adicionada aqui.')
    
    def __str__(self):
        return f"{self.codigo} - {self.nome}"
