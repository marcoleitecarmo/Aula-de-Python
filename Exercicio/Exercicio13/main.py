from cliente import Cliente
from banco import Banco
from contas import ContaCorrente, ContaPoupanca

banco = Banco()

cliente1 = Cliente('Luiz', 30)
cliente2 = Cliente('Maria', 18)
cliente3 = Cliente('João', 50)

conta1 = ContaPoupanca(1111, 254136, 0)
conta2 = ContaCorrente(2222, 267310, 250)
conta3 = ContaPoupanca(3333, 315784, 500)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_clientes(cliente1)
banco.inserir_conta(conta1)
banco.inserir_clientes(cliente2)
banco.inserir_conta(conta2)


if banco.autenticar(cliente1):
    cliente1.conta.depositar(40)
    cliente1.conta.sacar(20)
else:
    print('Cliente não autenticado')

print('*' * 100)

if banco.autenticar(cliente2):
    cliente2.conta.depositar(40)
    cliente2.conta.sacar(300)
else:
    print('Cliente não autenticado')