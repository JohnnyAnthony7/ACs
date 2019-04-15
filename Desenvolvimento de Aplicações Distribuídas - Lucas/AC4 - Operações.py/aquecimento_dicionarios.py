
reviews_aquecimento = [
    {
        'film_id': 'tt0076759',
        'user_id': 'marcos',
        'comment': 'gostei'
    },
    {
        'film_id': 'tt0076759',
        'user_id': 'lucio',
        'comment': 'achei legal'
    },
    {
        'film_id': 'tt1211837',
        'user_id': 'lucio',
        'comment': 'estranho'
    }
]

'''
A proxima atividade vai ter tudo a ver com essa
estrutura acima.

A idéia é que ela representa uma lista
de avaliacoes que os usuarios fizeram,
dando sua opiniao sobre alguns filmes.

Cada avaliacao está representada
como um dicionario com 3 chaves
'''

'''
primeiramente, façamos uma funcao
consulta que, dados o film_id e o user_id
devolve o dicionario da avaliacao
'''

def consulta(film_id,user_id):
    for x in range(len(reviews_aquecimento)):
        if ((film_id==reviews_aquecimento[x]['film_id']) and
        (user_id==reviews_aquecimento[x]['user_id'])):
            return reviews_aquecimento[x]
        else:
            return 'nao encontrado'
        
'''
Agora, façamos uma funcao que adiciona uma nova avaliacao
'''

def adiciona(film_id,user_id,comment):
    pass

'''
Agora, façamos um upgrade na adiciona:
    se o usuario ja avaliou esse filme,
    ao inves de adicionar uma nova avaliacao,
    mudamos a avaliacao existente.
'''
