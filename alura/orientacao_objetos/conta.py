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

    def saca(self, valor):
        self.__saldo -= valor

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


conta = Conta(12, 'larissa', 500, 8000)
