# core/vocabulary.py

VOCABULARY_CONTEXTS = {
    'supermercado': [
        {
            'word': 'carrinho',
            'translation': 'shopping cart',
            'examples': ['Você precisa de um carrinho?', 'O carrinho está cheio.'],
            'difficulty': 'A1'
        },
        {
            'word': 'cesta',
            'translation': 'basket',
            'examples': ['Pegue uma cesta para poucas compras.', 'A cesta está na entrada.'],
            'difficulty': 'A1'
        },
        {
            'word': 'prateleira',
            'translation': 'shelf',
            'examples': ['O produto está na prateleira de cima.', 'Procure na prateleira de ofertas.'],
            'difficulty': 'A2'
        },
        {
            'word': 'caixa',
            'translation': 'cashier/checkout',
            'examples': ['Vamos para o caixa.', 'Qual caixa está mais vazio?'],
            'difficulty': 'A1'
        },
        {
            'word': 'oferta',
            'translation': 'sale/offer',
            'examples': ['Este produto está em oferta.', 'Aproveite as ofertas da semana.'],
            'difficulty': 'A2'
        },
        {
            'word': 'desconto',
            'translation': 'discount',
            'examples': ['Tem desconto à vista?', 'O desconto é de 10%.'],
            'difficulty': 'A2'
        },
        {
            'word': 'promoção',
            'translation': 'promotion',
            'examples': ['Hoje tem promoção de frutas.', 'Esta promoção é por tempo limitado.'],
            'difficulty': 'A2'
        },
        {
            'word': 'preço',
            'translation': 'price',
            'examples': ['Qual é o preço deste item?', 'O preço está bom.'],
            'difficulty': 'A1'
        },
        {
            'word': 'sacola',
            'translation': 'bag',
            'examples': ['Precisa de sacola?', 'Trouxe minha sacola retornável.'],
            'difficulty': 'A1'
        },
        {
            'word': 'fila',
            'translation': 'queue/line',
            'examples': ['A fila está grande.', 'Vamos para esta fila.'],
            'difficulty': 'A1'
        }
    ],
    'café': [
        {
            'word': 'cardápio',
            'translation': 'menu',
            'examples': ['Posso ver o cardápio?', 'O cardápio tem muitas opções.'],
            'difficulty': 'A1'
        },
        {
            'word': 'pedido',
            'translation': 'order',
            'examples': ['Qual é o seu pedido?', 'Posso fazer o pedido?'],
            'difficulty': 'A1'
        },
        {
            'word': 'conta',
            'translation': 'bill',
            'examples': ['Por favor, a conta.', 'Pode trazer a conta?'],
            'difficulty': 'A1'
        },
        {
            'word': 'garçom',
            'translation': 'waiter',
            'examples': ['Chame o garçom, por favor.', 'O garçom está vindo.'],
            'difficulty': 'A1'
        },
        {
            'word': 'mesa',
            'translation': 'table',
            'examples': ['Tem mesa disponível?', 'Prefiro aquela mesa.'],
            'difficulty': 'A1'
        },
        {
            'word': 'sobremesa',
            'translation': 'dessert',
            'examples': ['Vamos pedir sobremesa?', 'Qual sobremesa você recomenda?'],
            'difficulty': 'A2'
        },
        {
            'word': 'gorjeta',
            'translation': 'tip',
            'examples': ['Vou deixar uma gorjeta.', 'A gorjeta já está incluída?'],
            'difficulty': 'B1'
        },
        {
            'word': 'reserva',
            'translation': 'reservation',
            'examples': ['Preciso fazer uma reserva?', 'Tenho uma reserva para duas pessoas.'],
            'difficulty': 'A2'
        },
        {
            'word': 'ambiente',
            'translation': 'atmosphere',
            'examples': ['O ambiente é agradável.', 'Gosto do ambiente deste café.'],
            'difficulty': 'B1'
        },
        {
            'word': 'especialidade',
            'translation': 'specialty',
            'examples': ['Qual é a especialidade da casa?', 'Este café é nossa especialidade.'],
            'difficulty': 'B1'
        }
    ]
}

def get_vocabulary_by_context(context: str, difficulty: str = None) -> list:
    """Retorna vocabulário filtrado por contexto e dificuldade."""
    if context not in VOCABULARY_CONTEXTS:
        return []
    
    vocabulary = VOCABULARY_CONTEXTS[context]
    if difficulty:
        vocabulary = [word for word in vocabulary if word['difficulty'] == difficulty]
    
    return vocabulary

def get_all_contexts() -> list:
    """Retorna todos os contextos disponíveis."""
    return list(VOCABULARY_CONTEXTS.keys())

def get_word_details(context: str, word: str) -> dict:
    """Retorna detalhes de uma palavra específica em um contexto."""
    if context not in VOCABULARY_CONTEXTS:
        return None
    
    for word_data in VOCABULARY_CONTEXTS[context]:
        if word_data['word'].lower() == word.lower():
            return word_data
    
    return None