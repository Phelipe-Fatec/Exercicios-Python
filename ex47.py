def dados(n='desconhecido', g=0):
    print(f"Jogador {n} tem {g} gols")

nome = str(input("Digite o nome do jogador: "))
gols = str(input("Digite a quantidade de gols do jogador: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    dados(g=gols)
else:
    dados(nome, gols)


