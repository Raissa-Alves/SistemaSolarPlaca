from django import forms
from solar.models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            'codigo', 
            'nome', 
            'imagem', 
            'preco', 
            'Q_Estoque', 
            'Forma_Pagamento', 
            'categoria', 
            'descricao'
        ]
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
            'preco': forms.NumberInput(attrs={'step': '0.01'}),
        }
    
    def clean_codigo(self):
        codigo = self.cleaned_data['codigo']
        if Produto.objects.filter(codigo=codigo).exists():
            raise forms.ValidationError("Este código já está em uso.")
        return codigo