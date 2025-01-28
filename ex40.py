def area(larg, comp):
    a = larg * comp
    print(f"A area do terreno de {larg}m² X {comp}m² é de {a:.1f}m²")

larg = float(input("Digite a largura do terreno: "))
comp = float(input("Digite o comprimento do terreno: "))
area(larg, comp)