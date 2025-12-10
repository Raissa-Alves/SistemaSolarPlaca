def carrinho_context(request):
    """Adiciona o carrinho ao contexto de todos os templates"""
    carrinho = request.session.get('carrinho', {})
    total_itens = sum(item['quantidade'] for item in carrinho.values())
    total_preco = sum(item['quantidade'] * item['preco'] for item in carrinho.values())
    
    return {
        'carrinho': carrinho,
        'total_itens_carrinho': total_itens,
        'total_preco_carrinho': total_preco,
    }