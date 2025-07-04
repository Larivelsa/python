class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo {self.__saldo} do titular {self.titular}")

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f"Não foi possível realiza o saque de R$ {valor}.")

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property  # getter
    def limite(self):
        return self.__limite

    @limite.setter  # setter
    def limite(self, limite):
        self.__limite = limite

    # métodos estáticos são métodos da classe
    # (todos objetos compartilham os mesmos métodos) e não do objeto
    # a forma de chamar o método é assim: Classe.metodo_estatico()
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}


conta = Conta(12, 'larissa', 500, 1000)
Conta.codigos_bancos()
conta.saca(200080)
