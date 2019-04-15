class ClienteNaoEncontradoException(Exception):
    pass #nao precisa fazer nada nessa classe, ela ja define a excessao nova

clientes_inicial = [
        {'id': 1, 'nome': "Cliente Um", 'email': "1@cliente.com", "saldo": 10},
        {'id': 2, 'nome': "Cliente Dois", 'email': "2@cliente.com", "saldo": 20},
        {'id': 3, 'nome': "Cliente Tres", 'email': "3@cliente.com", "saldo": 30},
        {'id': 4, 'nome': "Cliente Quatro", 'email': "4@cliente.com", "saldo": 40},
        {'id': 5, 'nome': "Cliente Cinco", 'email': "5@cliente.com", "saldo": 50}
    ]
def nro_clientes(clientes_inicial):
    return len(clientes_inicial)


def pesquisar_cliente(clientes_inicial, id):
    indices = list(range(len(clientes_inicial)))
    for x in indices:
        if(clientes_inicial[x]['id'] == id):
            return clientes_inicial[x]
    raise (ClienteNaoEncontradoException)

def excluir_cliente(clientes_inicial, id):
    indices = list(range(len(clientes_inicial)))
    for x in indices:
        if(clientes_inicial[x]['id'] == id):
            del(clientes_inicial[x]) 
            break
