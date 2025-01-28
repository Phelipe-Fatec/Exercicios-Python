listjogador = []
listaux = []
jogador = {}
while True:
    jogador['nome'] = str(input("Digite o nome do jogador: "))
    partidas = int(input(f"Digite a quantidade de partidas que {jogador['nome']} jogou: "))
    jogador['gols'] = []
    for g in range(0, partidas):
        gols = int(input(f"Quantos gols na partida {g}: "))
        jogador['gols'].append(gols)
    jogador['total'] = sum(jogador['gols'])
    listjogador.append(jogador.copy())
    jogador.clear()
    continuar = str(input("Deseja continuar? [S/N]: ")).strip().upper()
    while continuar not in 'SsNn':
        print("Inválido")
        continuar = str(input("Deseja continuar? [S/N]: ")).strip().upper()
    if continuar in 'Nn':
        break

print('-=' * 30)
for k, v in enumerate(listjogador):
    print(f"código do jogador: {k} nome: {v['nome']} gols: {v['gols']} total: {v['total']}")
    listaux.append(k)
listaux.append(999)
while True:
    dadosjogador = int(input("Levantar dados de qual jogador? (999 para parar) "))
    while dadosjogador not in listaux:
        print("Inválido")
        dadosjogador = int(input("Levantar dados de qual jogador? (999 para parar) "))
    if dadosjogador == 999:
        break
    print(f"Levantamento do jogador {listjogador[dadosjogador]['nome']}")
    for d in range(0, len(listjogador[dadosjogador]['gols'])):
        print(f"No jogo {d} fez {listjogador[dadosjogador]['gols'][d]} gols")

