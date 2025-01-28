import random
import time
import operator
jogo = {'jogador1': random.randint(1, 6),
        'jogador2': random.randint(1, 6),
        'jogador3': random.randint(1, 6),
        'jogador4': random.randint(1, 6)}

for j, v in jogo.items():
    print(f"{j} tirou {v} no dado")
    time.sleep(0.7)

ranking = sorted(jogo.items(), key=operator.itemgetter(1), reverse=True)

for j, v in enumerate(ranking):
    print(f"{j + 1}º Lugar: {v[0]} - {v[1]}")