class Teste:
    def __init__(self, valor):
        self.valor = valor

    def get_valor(self):
        return self.valor

    def set_valor(self, dif):
        self.valor = dif

valor = Teste(10)
print(valor.get_valor())

novo_Valor = int(input("Digite um novo número para o objeto: "))

valor = novo_Valor

print(valor)