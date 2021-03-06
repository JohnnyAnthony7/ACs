#!bin/python
from flask import Flask,jsonify,abort
from flask import make_response, request
import acesso_omdb


app = Flask(__name__)

reviews = [
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

notas = [
    {
        'film_id': 'tt0076759',
        'user_id': 'marcos',
        'stars': 4
    },
    {
        'film_id': 'tt0076759',
        'user_id': 'lucio',
        'stars': 5
    },
    {
        'film_id': 'tt1211837',
        'user_id': 'lucio',
        'stars': 2
    }
]

'''
Primeira coisa:
    certifique-se que todos os arquivos que voce baixou
    do classroom estao na mesma pasta
    se nao, nao vai rodar
'''


'''
Você consegue abrir a pagina que geramos abaixo?

Mesmo dando problema com a firewall,
voce deve conseguir vê-la em http://localhost:5001
'''
@app.route('/')
def index():
  return "SocialFilm!"
'''
Vou deixar essa rota pronta pra vocês, para vocês poderem debugar mais facil

Ela imprime tudo que esta guardado no servidor
'''
@app.route('/socialfilm/all/', methods=['GET'])
def tudo():
   return jsonify({'reviews':reviews,'notas':notas})


'''
Ler reviews existentes
    ao acessar a URL /socialfilm/reviews/id_filme/id_usuario com o metodo GET,
    podemos ler a review do usuario para aquele filme
    
    O retorno deve ser um dicionario, com as chaves 'user_id' e 'comment',
    que sao, respectivamente, a id do usuario e o comentario
    
    Você pode percorrer o objeto "reviews" com um for. Se acontecer
    de algum elemento lá dentro ter film_id igual à passada na url
    e user_id igual ao passado na url, retorne o comentario.

    Se voce nao achar a review, retorne
    um dicionario com a chave 'erro' associada ao valor "comentario nao encontrado"
    Nesse caso de review invalida, também retorne um codigo de status 404
@app.route('/socialfilm/reviews/<film_id>/<user_id>', methods=['GET'])
'''

@app.route('/socialfilm/reviews/<film_id>/<user_id>', methods=['GET'])
def get_review(film_id,user_id):
    for x in range (len(reviews)):
        if film_id==reviews[x]['film_id'] and user_id==reviews[x]['user_id']:
            return jsonify({"user_id":user_id, "comment":reviews[x]['comment']})
    return jsonify({"erro":"comentario nao encontrado"}),404


'''
Adicionar um comentario:
    ao acessar a URL /socialfilm/reviews/id_filme/id_usuario com o metodo PUT, 
    podemos adicionar (ou trocar) a review do usuario.

    Metodo PUT??
    Nao se preocupe, do ponto de vista de acessar as variaveis
    enviadas, o PUT e o POST sao iguais.

    A (nova) review vem num objeto que vem no body do request
    Um dicionario que  tem a chave 'comment' e o valor sendo
    o texto desse comentario

    Cuidado! Se o usuário já fez review daquele filme, troque, nao 
    adicione outra

    Você pode percorrer o objeto "reviews" com um for. Se acontecer
    de algum elemento lá dentro ter film_id igual à passada na url
    e user_id igual ao passado na url, mude o comentario. 
    (isso é, mantenha o dicionário e altere apenas a chave "comment")

    Caso contrario, adicione.

    Retorne o objeto da review adicionada
@app.route('/socialfilm/reviews/<film_id>/<user_id>', methods=['PUT'])
'''
@app.route('/socialfilm/reviews/<film_id>/<user_id>', methods=['PUT'])
def put_review(film_id,user_id):
    dici=request.json
    for x in range (len(reviews)):
        if film_id==reviews[x]['film_id'] and user_id==reviews[x]['user_id']:
            reviews[x]['comment']=dici['comment']
            return jsonify({"film_id":film_id,"user_id":user_id,"comment":dici['comment']})
    reviews.append({"film_id":film_id,"user_id":user_id,"comment":dici['comment']})
    return jsonify({"film_id":film_id,"user_id":user_id,"comment":dici['comment']})

'''
quando acessarmos a url /socialfilm/reviews/all_films/<user_id> com o metodo GET,
devemos receber todas as reviews feitas pelo usuario.

Ou seja, uma lista de dicionarios, cada um deles representando uma review. 
Cada dicionário tem que ter as chaves "film_id" "user_id" e "comment"
'''
@app.route('/socialfilm/reviews/all_films/<user_id>', methods=['GET'])
def all_reviews(user_id):
    todasReviews=[]
    for x in range(len(reviews)):
        if reviews[x]['user_id']==user_id:
            todasReviews.append({"film_id":reviews[x]["film_id"], "user_id":reviews[x]["user_id"],
            "comment":reviews[x]["comment"]})
    return jsonify(todasReviews)


'''
Agora, façamos a parte das estrelas:
    /socialfilm/stars/film_id/user_id deve poder receber GET (para lermos quantas 
    estrelas um usuário deu a um filme) 

    retorne o dicionaro {"error":"filme nao encontrado"} se o filme nao existir
    nos OMDB, e {"error":"review nao encontrada"} se o usuário nao tiver
    dado estrelas para esse filme. Em ambos os casos, o status code
    http deve ser 404
'''
@app.route('/socialfilm/stars/<film_id>/<user_id>', methods=['GET'])
def retorna_estrelas(film_id,user_id):
    for x in range(len(notas)):
        if film_id==notas[x]["film_id"] and user_id==notas[x]["user_id"] and (len(str(notas[x]["stars"]))>0):
            return jsonify({"stars":notas[x]["stars"]})
    return jsonify({"error":"review nao encontrada"}),404          
        


'''
Também devemos conseguir salvar estrelas, com PUT. O usuário
poderá alterar as estrelas que deu para um filme, ou avaliar um
filme que nao avaliou ainda

    No caso do PUT, o usuário envia no body um dicionario {"stars":num}, 
    onde num vai de 0 a 5.
    Retorne um erro 400 se num nao for válido ou se "stars" nao for uma chave
    do dicionario
'''


@app.route('/socialfilm/stars/<film_id>/<user_id>', methods=['PUT'])
def add_estrelas(film_id,user_id):
    dici=request.json
    for x in range(len(notas)):
        if film_id==notas[x]["film_id"] and user_id==notas[x]["user_id"]:
            notas[x]["stars"]=dici["stars"]
            return jsonify({"film_id":film_id, "user_id":user_id, "stars":dici['stars']})
    notas.append({"film_id":film_id, "user_id":user_id, "stars":dici['stars']})
    return jsonify({"film_id":film_id, "user_id":user_id, "stars":dici['stars']})

'''
Para vermos a média de estrelas de um filme, podemos acessar a URL
/socialfilm/stars/film_id/average com GET.

O retorno é um json: {"average_stars": num} onde num é a media
do numero de estrelas que os usuários deram para o filme,
ou 'nao avaliado' se nenhum usuário avaliou o filme ainda
'''
@app.route('/socialfilm/stars/<film_id>/average', methods=['GET'])
def retorna_media(film_id):
    notasFilme=[]
    for x in range(len(notas)):
        if film_id==notas[x]["film_id"]:
            notasFilme.append(notas[x]["stars"])
    media=sum(notasFilme)/len(notasFilme)
    return jsonify({"average_stars":media})

'''
Agora, chegou a hora de integrar seu servidor ao OMDB

Va ao arquivo acesso_omdb.py e crie a funcao existe_id

Depois, altere a funcao de adicionar reviews 
para dar um erro quando voce tentou fazer
uma review de um filme que nao existe no banco de dados:

A função deve retornar o json {"error":"filme nao encontrado"} 
e dar um cod status http 404

Para acessar a funcao que voce definiu no acesso_omdb, 
basta usar acesso_omdb.existe_id(sua_id)
'''

'''
Agora, vamos pegar a funcao all_reviews 
(da url all_films) e melhorar: 
A funcao devolve um dicionario para cada review.
Consultando
o OMDB, podemos adicionar o nome do filme em cada um desses dicionarios.

O nome do filme deverá vir na chave film_name.

Antes de mais nada, va no acesso_omdb e defina a função pega_nome

Entao, use a função para adicionar o film_name no dicionario de cada filme 
retornado pela funcao anterior

Tome cuidado: nao queremos alternar os dados locais. 
Verifique que o vetor reviews nao esta recebendo esses nomes

Voce talvez queira aprender a copiar dicionarios em python
'''

'''
Uma ultima mudança: não deixe o usuário adicionar estrelas para filmes 
que nao existem no OMDB. Isso vai ser muito parecido com a integracao
que você já fez para as reviews
'''

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5001)
