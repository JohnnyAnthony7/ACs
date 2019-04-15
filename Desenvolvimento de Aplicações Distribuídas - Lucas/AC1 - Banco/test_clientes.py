#from estruturado.MeusModulos.Clientes import *
from estruturado.MeusModulos import Clientes
import copy
#adicione um import para acessar o módulo ContaCorrente
from estruturado.MeusModulos import ContaCorrente
import unittest

class TestClientes(unittest.TestCase):
    def test_01_list(self):
        self.assertEqual(Clientes.nro_clientes(Clientes.clientes_inicial), 5)

    def test_02_list(self):
        clientes_copia = copy.deepcopy(Clientes.clientes_inicial)
        Clientes.excluir_cliente(clientes_copia, 3)
        self.assertEqual(Clientes.nro_clientes(clientes_copia), 4)

    def test_03_busca_acha(self):
        cliente = Clientes.pesquisar_cliente(Clientes.clientes_inicial, 1)
        if type(cliente) != dict:
            self.fail('nao achei o cliente 1')
        cliente_3 = Clientes.pesquisar_cliente(Clientes.clientes_inicial, 1)
        if type(cliente_3) != dict:
            self.fail('nao achei o cliente 3')

    def test_04_busca_excessao(self):
        try:
            Clientes.pesquisar_cliente(Clientes.clientes_inicial,10)
        except Clientes.ClienteNaoEncontradoException:
            print('ok, sua busca por cliente 10 retornou excessao, como devia')
        except:
            self.fail('sua busca por cliente 10 retornou excessao, mas nao a correta')
        else:
            self.fail('sua busca por cliente 10 nao retornou excessao')

    def test_05_credito(self):
        clientes_copia = copy.deepcopy(Clientes.clientes_inicial)
        cliente = Clientes.pesquisar_cliente(clientes_copia, 1)
        ContaCorrente.credito(10, cliente, 10, 10)
        self.assertEqual(cliente['saldo'], 20)

    def test_06_debito(self):
        clientes_copia = copy.deepcopy(Clientes.clientes_inicial)
        cliente = Clientes.pesquisar_cliente(clientes_copia, 1)
        ContaCorrente.debito(10, cliente, 10, 10)
        self.assertEqual(cliente['saldo'], 0)
    
    def test_07_debito_negativando(self):
        clientes_copia = copy.deepcopy(Clientes.clientes_inicial)
        cliente = Clientes.pesquisar_cliente(clientes_copia, 3)
        ContaCorrente.debito(30, cliente, 10, 30)
        self.assertEqual(cliente['saldo'], 0)
        ContaCorrente.debito(10, cliente, 10, 10) #saque da conta zerada, mas o terceiro parametro,
        #limite_credito, diz que pode
        self.assertEqual(cliente['saldo'], -10)
    
    def test_08_debito_alem_do_limite(self):
        clientes_copia = copy.deepcopy(Clientes.clientes_inicial)
        cliente = Clientes.pesquisar_cliente(clientes_copia, 2)
        ContaCorrente.debito(20, cliente, 10, 20)
        self.assertEqual(cliente['saldo'], 0)
        ContaCorrente.debito(10, cliente, 10, 10) #saque da conta zerada, mas o terceiro parametro,
        #limite_credito, diz que pode
        self.assertEqual(cliente['saldo'], -10)
        try:
            ContaCorrente.debito(10, cliente, 10, 10) #estou excedendo o limite
        except:
            print('ok, voce deu uma excessao quando o limite foi excedido')
        else: #se nao rolou excessao
            self.fail('voce nao deu uma excessao quando excedemos o limite')
        self.assertEqual(cliente['saldo'], -10) #verificar se vc nao debitou a
        #operacao invalida

    def test_09_transferencia_funciona(self):
        clientes_copia = copy.deepcopy(Clientes.clientes_inicial)
        doador,receptor = 2,5
        valor_doado = 20
        limite_credito, limite_transferencia = 0,100
        ContaCorrente.transferencia(clientes_copia,doador,receptor,valor_doado,limite_credito,limite_transferencia)
        self.assertEqual(Clientes.pesquisar_cliente(clientes_copia,2)['saldo'],0)
        self.assertEqual(Clientes.pesquisar_cliente(clientes_copia,5)['saldo'],70)
    
    def test_10_transferencia_falha_limite_credito(self):
        clientes_copia = copy.deepcopy(Clientes.clientes_inicial)
        doador,receptor = 2,5
        valor_doado = 30
        limite_credito, limite_transferencia = 0,100
        try:
            ContaCorrente.transferencia(clientes_copia,doador,receptor,valor_doado,limite_credito,limite_transferencia)
        except ContaCorrente.LimiteCreditoExcedidoException:
            print('ao usar credito demais, a transferencia falha com a excessao correta')
        except:
            self.fail('ao usar credito demais, a transferencia falhou com a excessao errada')
        else:
            self.fail('ao usar credito demais, a transferencia nao levantou excessao')

        self.assertEqual(Clientes.pesquisar_cliente(clientes_copia,2)['saldo'],20)
        self.assertEqual(Clientes.pesquisar_cliente(clientes_copia,5)['saldo'],50)
    
    def test_11_transferencia_falha_limite_transferencia(self):
        clientes_copia = copy.deepcopy(Clientes.clientes_inicial)
        doador,receptor = 2,5
        valor_doado = 20
        limite_credito, limite_transferencia = 10,10
        try:
            ContaCorrente.transferencia(clientes_copia,doador,receptor,valor_doado,limite_credito,limite_transferencia)
        except ContaCorrente.LimiteTransferenciaExcedidoException:
            print('ao ultrapassar o limite de transferencia, a transferencia falha com a excessao correta')
        except:
            self.fail('ao ultrapassar o limite de transferencia, a transferencia falha com a excessao errada')
        else:
            self.fail('ao ultrapassar o limite de transferencia, a transferencia nao falhou, mas devia')

        self.assertEqual(Clientes.pesquisar_cliente(clientes_copia,2)['saldo'],20)
        self.assertEqual(Clientes.pesquisar_cliente(clientes_copia,5)['saldo'],50)
        
            


def run_tests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestClientes)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

if __name__ == '__main__':
    run_tests()
