jogador = {}

jogador['nome'] = str(input("Digite o nome do jogador: "))
partidas = int(input(f"Digite a quantidade de partidas que {jogador['nome']} jogou: "))
jogador['gols'] = []
for g in range(0, partidas):
    gols = int(input(f"Quantos gols na partida {g}: "))
    jogador['gols'].append(gols)
jogador['total'] = sum(jogador['gols'])

print("=-" * 30)
print(jogador)

print("=-" * 30)
for k, v in jogador.items():
    print(f"O campo {k} tem valor {v}")

print("=-" * 30)
print(f"O jogador {jogador['nome']} jogou {partidas} partidas.")
for k, v in enumerate(jogador['gols']):
    print(f"  => Na partida {k} ele marcou {v} gols.")
print(f"Foi um total de {jogador['total']} gols.")