import teste

número = int(input("Digite um número: "))
print(f"O dobro de {número} é {teste.moeda(teste.dobro(número))}")
print(f"A metade de {número} é {teste.moeda(teste.metade(número))}")
print(f"A soma de 10% de {número} é {teste.moeda(teste.aumentar(número))}")
print(f"A subtração de 10% de {número} é {teste.moeda(teste.diminuir(número))}")