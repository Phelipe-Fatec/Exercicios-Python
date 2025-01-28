import teste

número = int(input("Digite um número: "))
taxa = int(input("Digite a taxa: "))
print(f"O dobro de {número} é {teste.dobro(número, True)}")
print(f"A metade de {número} é {teste.metade(número, True)}")
print(f"A soma de {taxa}% de {número} é {teste.aumentar(número, taxa, True)}")
print(f"A subtração de {taxa}% de {número} é {teste.diminuir(número, taxa, True)}")