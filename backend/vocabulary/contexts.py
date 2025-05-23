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
    ],
    'directions': [
        {'word': 'left', 'translation': 'esquerda', 'examples': ['Turn left at the corner.', 'The bank is on the left.'], 'difficulty': 'A1'},
        {'word': 'right', 'translation': 'direita', 'examples': ['The pharmacy is on your right.', 'Take the next right.'], 'difficulty': 'A1'},
        {'word': 'straight ahead', 'translation': 'em frente', 'examples': ['Go straight ahead for two blocks.', 'Keep going straight ahead.'], 'difficulty': 'A1'},
        {'word': 'corner', 'translation': 'esquina', 'examples': ['The shop is on the corner.', 'Meet me at the corner of Main and First Street.'], 'difficulty': 'A2'},
        {'word': 'block', 'translation': 'quarteirão', 'examples': ['Walk two blocks and then turn left.', 'The museum is just one block away.'], 'difficulty': 'A2'},
        {'word': 'map', 'translation': 'mapa', 'examples': ["Can you show me on the map?", "I'll check the map on my phone."], 'difficulty': 'A1'},
        {'word': 'address', 'translation': 'endereço', 'examples': ["What's your address?", "I need the full address."], 'difficulty': 'A2'},
        {'word': 'near', 'translation': 'perto', 'examples': ['Is there a post office near here?', 'The station is quite near.'], 'difficulty': 'A1'},
        {'word': 'far', 'translation': 'longe', 'examples': ['Is it far to walk?', 'The airport is far from the city center.'], 'difficulty': 'A1'},
        {'word': 'landmark', 'translation': 'ponto de referência', 'examples': ['Use the tall tower as a landmark.', 'Common landmarks include churches and statues.'], 'difficulty': 'B1'}
    ],
    'phone_calls': [
        {'word': 'call', 'translation': 'ligar/chamada', 'examples': ["I need to make a call.", "I missed a call from you."], 'difficulty': 'A1'},
        {'word': 'phone number', 'translation': 'número de telefone', 'examples': ["What's your phone number?", "Can I have your phone number?"], 'difficulty': 'A1'},
        {'word': 'to ring', 'translation': 'tocar (telefone)', 'examples': ['The phone is ringing.', "I heard my phone ring."], 'difficulty': 'A2'},
        {'word': 'to answer', 'translation': 'atender (telefone)', 'examples': ['Could you answer the phone?', 'She answered on the third ring.'], 'difficulty': 'A2'},
        {'word': 'to hang up', 'translation': 'desligar (telefone)', 'examples': ['Don_t hang up on me!', 'He hung up before I could reply.'], 'difficulty': 'B1'},
        {'word': 'busy line', 'translation': 'linha ocupada', 'examples': ["I tried calling, but the line was busy.", "It's frustrating to get a busy line."], 'difficulty': 'B1'},
        {'word': 'voicemail', 'translation': 'correio de voz', 'examples': ['Please leave a message on my voicemail.', 'I need to check my voicemail.'], 'difficulty': 'A2'},
        {'word': 'leave a message', 'translation': 'deixar uma mensagem', 'examples': ["Could I leave a message for him?", "He wasn't there, so I left a message."], 'difficulty': 'A2'}
    ],
    'public_transport': [
        {'word': 'bus', 'translation': 'ônibus', 'examples': ['I take the bus to work.', 'The next bus arrives in 10 minutes.'], 'difficulty': 'A1'},
        {'word': 'train', 'translation': 'trem', 'examples': ['The train to London is delayed.', 'We bought train tickets online.'], 'difficulty': 'A1'},
        {'word': 'subway', 'translation': 'metrô', 'examples': ["Let's take the subway, it's faster.", 'The subway station is nearby.'], 'difficulty': 'A2'},
        {'word': 'ticket', 'translation': 'passagem/bilhete', 'examples': ['I need to buy a ticket.', 'Can I see your ticket, please?'], 'difficulty': 'A1'},
        {'word': 'platform', 'translation': 'plataforma', 'examples': ['The train will depart from platform 3.', 'Which platform is it for the airport train?'], 'difficulty': 'A2'},
        {'word': 'stop', 'translation': 'parada/ponto', 'examples': ['This is my stop.', 'The bus stop is just around the corner.'], 'difficulty': 'A1'},
        {'word': 'fare', 'translation': 'tarifa', 'examples': ["What's the bus fare?", 'The train fare has increased.'], 'difficulty': 'B1'},
        {'word': 'route', 'translation': 'rota/linha', 'examples': ['Which bus route goes to the city center?', 'This is the scenic route.'], 'difficulty': 'B1'},
        {'word': 'schedule', 'translation': 'horário/programação', 'examples': ["Let's check the train schedule.", 'The bus is not on schedule today.'], 'difficulty': 'A2'},
        {'word': 'one-way', 'translation': 'só ida', 'examples': ['A one-way ticket, please.', 'Is this a one-way street?'], 'difficulty': 'A2'},
        {'word': 'round trip', 'translation': 'ida e volta', 'examples': ['A round trip ticket is usually cheaper.', 'I need a round trip ticket to Paris.'], 'difficulty': 'A2'}
    ],
    'health': [
        {'word': 'headache', 'translation': 'dor de cabeça', 'examples': ['I have a bad headache.', 'She took medicine for her headache.'], 'difficulty': 'A1'},
        {'word': 'cold', 'translation': 'resfriado', 'examples': ['I think I caught a cold.', "He's staying home because of a cold."], 'difficulty': 'A1'},
        {'word': 'flu', 'translation': 'gripe', 'examples': ['The flu can be serious.', 'Symptoms of the flu include fever and body aches.'], 'difficulty': 'A2'},
        {'word': 'fever', 'translation': 'febre', 'examples': ['He has a high fever.', 'Check your temperature if you feel a fever.'], 'difficulty': 'A1'},
        {'word': 'cough', 'translation': 'tosse', 'examples': ['She has a persistent cough.', 'This cough syrup should help.'], 'difficulty': 'A2'},
        {'word': 'pain', 'translation': 'dor', 'examples': ['I have a pain in my back.', 'Where do you feel the pain?'], 'difficulty': 'A1'},
        {'word': 'pharmacy', 'translation': 'farmácia', 'examples': ["I need to go to the pharmacy.", 'You can buy this medicine at any pharmacy.'], 'difficulty': 'A2'},
        {'word': 'doctor', 'translation': 'médico(a)', 'examples': ["You should see a doctor.", "My doctor's appointment is at 3 PM."], 'difficulty': 'A1'},
        {'word': 'appointment', 'translation': 'consulta/compromisso', 'examples': ['I need to make a doctor_s appointment.', 'Her appointment is scheduled for tomorrow.'], 'difficulty': 'A2'},
        {'word': 'prescription', 'translation': 'receita médica', 'examples': ['This medicine requires a prescription.', 'The doctor gave me a prescription for antibiotics.'], 'difficulty': 'B1'},
        {'word': 'medicine', 'translation': 'remédio', 'examples': ['Have you taken your medicine?', 'This medicine helps with the pain.'], 'difficulty': 'A1'}
    ],
    'social_talk': [
        {'word': 'weather', 'translation': 'tempo/clima', 'examples': ["The weather is nice today, isn't it?", "What's the weather forecast for tomorrow?"], 'difficulty': 'A1'},
        {'word': 'hobbies', 'translation': 'hobbies/passatempos', 'examples': ['What are your hobbies?', 'Reading is one of my favorite hobbies.'], 'difficulty': 'A2'},
        {'word': 'weekend', 'translation': 'fim de semana', 'examples': ['What did you do over the weekend?', 'I_m looking forward to the weekend.'], 'difficulty': 'A1'},
        {'word': 'work', 'translation': 'trabalho', 'examples': ["How's work going?", "I have a lot of work to do."], 'difficulty': 'A1'},
        {'word': 'studies', 'translation': 'estudos', 'examples': ["How are your studies progressing?", "She's focused on her studies."], 'difficulty': 'A2'},
        {'word': 'interests', 'translation': 'interesses', 'examples': ['What are your main interests?', 'He has many different interests.'], 'difficulty': 'B1'},
        {'word': 'news', 'translation': 'notícias', 'examples': ["Have you heard the latest news?", "I usually watch the news in the evening."], 'difficulty': 'A2'},
        {'word': 'party', 'translation': 'festa', 'examples': ["Are you going to the party on Saturday?", "It was a great party!"], 'difficulty': 'A1'},
        {'word': 'concert', 'translation': 'show/concerto', 'examples': ['We went to a concert last night.', 'The band is giving a concert next month.'], 'difficulty': 'A2'},
        {'word': 'movie', 'translation': 'filme', 'examples': ['Have you seen any good movies lately?', 'Let_s go to the movies tonight.'], 'difficulty': 'A1'}
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