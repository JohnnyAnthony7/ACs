from flask import Flask, request, json, jsonify

app = Flask(__name__) 

database = {}
database['ALUNO'] = []

@app.route("/alunos", methods=['POST'])
def cria_aluno():
        dic = request.json
        database['ALUNO'].append(dic)
        return jsonify(database['ALUNO'])

@app.route("/alunos")
def lista_aluno():
        return jsonify(database['ALUNO'])

@app.route("/") 
def hello():
        print('rodei')
        return "Hello World!"


if __name__ == '__main__':
            app.run(host='localhost', port=5002, debug=True) 
