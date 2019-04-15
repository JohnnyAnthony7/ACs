from flask import Flask, request, jsonify
import requests
#from flask import *

app = Flask(__name__) 

database={}
database['ALUNO']=[]
database['PROFESSOR']=[]


#na url /alunos
#com verbo post
@app.route('/alunos', methods=['POST'])
def cria_aluno():
        dici = request.json
        check=possuiNome(dici)
        if check==False:
                return jsonify({"erro":"aluno sem nome"}),400
        check=idAlunoExiste(dici['id'])
        if check==True:
                return jsonify({"erro":"id ja utilizada"}),400
        database['ALUNO'].append(dici)
        return jsonify(database['ALUNO'])

@app.route('/professores', methods=['POST'])
def cria_professor():
        dici = request.json
        check=possuiNome(dici)
        if check==False:
                return jsonify({"erro":"professor sem nome"}),400
        check=idProfExiste(dici['id'])
        if check==True:
                return jsonify({"erro":"id ja utilizada"}),400
        database['PROFESSOR'].append(dici)
        return jsonify(database['PROFESSOR'])

@app.route('/alunos/<int:id_aluno>', methods=['DELETE'])
def deleta_aluno(id_aluno):
        check=idAlunoExiste(id_aluno)
        if check==False:
                return jsonify({"erro":"aluno nao encontrado"}),400
        for x in range(len(database['ALUNO'])):
                if id_aluno==database['ALUNO'][x]['id']:
                        del database['ALUNO'][x]

@app.route('/professores/<int:id_professor>', methods=['DELETE'])
def deleta_professor(id_professor):
        check=idProfExiste(id_professor)
        if check==False:
                return jsonify({"erro":"professor nao encontrado"}),400
        for x in range(len(database['PROFESSOR'])):
                if id_professor==database['PROFESSOR'][x]['id']:
                        del database['PROFESSOR'][x]

    
    

@app.route('/alunos', methods=['GET'])
def lista_alunos():
    return jsonify(database['ALUNO'])

@app.route('/professores', methods=['GET'])
def lista_professores():
    return jsonify(database['PROFESSOR'])

@app.route('/alunos/<int:id_aluno>', methods=['GET'])
def localiza_aluno(id_aluno):
        check=idAlunoExiste(id_aluno)
        if check==False:
                return jsonify({"erro":"aluno nao encontrado"}),400
        for aluno in database['ALUNO']:
                if aluno['id'] == id_aluno:
                        return jsonify(aluno)

@app.route('/professores/<int:id_professor>', methods=['GET'])
def localiza_professor(id_professor):
        check=idProfExiste(id_professor)
        if check==False:
                return jsonify({"erro":"professor nao encontrado"}),400
        for i in database['PROFESSOR']:
                if i['id'] == id_professor:
                        return jsonify(i)


@app.route('/professores/<int:id_professor>', methods=['PUT'])
def edita_prof(id_professor):
        check=idProfExiste(id_professor)
        if check==False:
                return jsonify({"erro":"professor nao encontrado"}),400
        dici=request.json
        check=possuiNome(dici)
        if check==False:
                return jsonify({"erro":"professor sem nome"}),400
        for x in range(len(database['PROFESSOR'])):
                if id_professor==database['PROFESSOR'][x]['id']:
                        database['PROFESSOR'][x]['nome']=dici['nome']

        
@app.route('/alunos/<int:id_aluno>', methods=['PUT'])
def edita_aluno(id_aluno):
        check=idAlunoExiste(id_aluno)
        if check==False:
                return jsonify({"erro":"aluno nao encontrado"}),400
        dici=request.json
        check=possuiNome(dici)
        if check==False:
                return jsonify({"erro":"aluno sem nome"}),400
        for x in range(len(database['ALUNO'])):
                if id_aluno==database['ALUNO'][x]['id']:
                        database['ALUNO'][x]['nome']=dici['nome']

@app.route('/reseta', methods=['POST'])
def reseta():
    database['ALUNO']=[]
    database['PROFESSOR']=[]
    return jsonify(database['ALUNO'])


        
@app.route("/") 
def hello():
        print('rodei')
        return "Hello World!"



#funções que fazem checagem
def idAlunoExiste(id):
        for x in range (len(database['ALUNO'])):
                if id==database['ALUNO'][x]['id']:
                        return True
        return False

def idProfExiste(id):
        for x in range (len(database['PROFESSOR'])):
                if id==database['PROFESSOR'][x]['id']:
                        return True
        return False

def possuiNome(dici):
        if not 'nome' in dici:
                return False
        return True



if __name__ == '__main__':
            app.run(host='localhost', port=5002, debug=True)
