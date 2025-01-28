class Gato:
    tipo_animal = 'Felino'

    def __init__(self, nome):
        self.nome = nome
        print(f"O nome do seu gato é {self.nome}")

    def peso_gato(self, peso):
        self.peso = peso
        if self.peso >= 5.0:
            print("Seu gato está gordinho")
        elif self.peso < 5.0 and peso > 3.5:
            print("Peso normal")
        else:
            print("O animal está abaixo do peso")

    def _dieta_especial_gato(self):
        self.msg = 'Tudo ok'
        if self.peso < 3.5:
            self.msg = 'Aumente a ração do gato'
        if self.peso >= 5.0:
            self.msg = 'Diminua a ração do gato'
        return self.msg

    def dados_gato(self):
        print(f"O gato {self.nome} tem {self.peso}Kg")
        print(self._dieta_especial_gato())


nome_gato = input("Digite o nome do gato: ")
g1 = Gato(nome_gato)

peso = float(input("Qual o peso do seu gato em KG: "))
g1.peso_gato(peso)

g1.dados_gato()
print(g1.tipo_animal)
