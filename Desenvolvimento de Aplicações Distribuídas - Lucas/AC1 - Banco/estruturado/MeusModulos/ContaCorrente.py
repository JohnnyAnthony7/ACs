from . import Clientes

class LimiteCreditoExcedidoException(Exception):
    pass #nao precisa fazer nada nessa classe, ela ja define a excessao nova

class LimiteTransferenciaExcedidoException(Exception):
    pass #crie aqui uma nova excessao LimiteTransferenciaExcedidoException

def credito(valor, cliente, limite_credito, limite_transferencia):
    cliente['saldo'] += valor

def debito(valor, cliente, limite_credito, limite_transferencia):
    vl = cliente['saldo'] + limite_credito
    if valor > vl:
        raise LimiteCreditoExcedidoException
    cliente['saldo'] -= valor


def transferencia(lista_clientes,id_cliente_doador,id_cliente_receptor,valor,limite_credito,limite_transferencia):
    doador = Clientes.pesquisar_cliente(lista_clientes, id_cliente_doador)
    receptor = Clientes.pesquisar_cliente(lista_clientes, id_cliente_receptor)
    if(valor > limite_transferencia):
        raise LimiteTransferenciaExcedidoException
    debito(valor, doador, limite_credito, limite_transferencia)
    credito(valor, receptor, limite_credito, limite_transferencia)

