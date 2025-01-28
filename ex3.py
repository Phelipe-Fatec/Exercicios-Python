ano = 2023
totalidade = 0
menor = 0
maisvelho = 0
for i in range (1, 5):
    nome = str(input(f"Digite o nome da {i} pessoa: "))
    idade = int(input(f"Digite o ano de nascimento da {i} pessoa: "))
    sexo = str(input(f"Digite o sexo da {i} pessoa (M para masculino e F para feminino): ")).upper()

    atual = ano - idade

    if sexo == 'M':
        if i == 1:
            maisvelho = atual
        else:
           if atual > maisvelho:
            maisvelho = atual

    if sexo == 'F':
        if atual < 20:
            menor += 1

print(f"{menor} mulheres são menores de idade")
print(f"O homem mais velho foi {maisvelho}")


#NÃO CONSEGUI FAZERKKKKKKK

