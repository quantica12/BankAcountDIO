class ContaBancaria:
    def __init__(self):
        self.saldo = 0.0

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    def extrato(self):
        print(f"Saldo atual: R${self.saldo:.2f}")


if __name__ == "__main__":
    conta = ContaBancaria()

    while True:
        print("\nEscolha uma operação:")
        print("1. Depósito")
        print("2. Saque")
        print("3. Extrato")
        print("4. Sair")

        opcao = int(input("Digite o número da operação desejada: "))

        if opcao == 1:
            valor_deposito = float(input("Digite o valor do depósito: "))
            conta.depositar(valor_deposito)
        elif opcao == 2:
            valor_saque = float(input("Digite o valor do saque: "))
            conta.sacar(valor_saque)
        elif opcao == 3:
            conta.extrato()
        elif opcao == 4:
            print("Obrigado por usar nosso sistema bancário!")
            break
        else:
            print("Opção inválida. Tente novamente.")
