import random
jogador = 0
cpu = 0
jogo = ''
soma = 0
vitoria = 0
print(f"{25 * '-='}")
print("VAMOS JOGAR PAR OU IMPAR")
print(f"{25 * '-='}")

while True:
    jogador = int(input("Digite um valor: "))
    jogo = str(input("Par ou impar? [P/I] ")).upper().strip()
    print(f"{25 * '--'}")
    cpu = random.randint(1, 100)
    soma = jogador + cpu
    print(f"Você jogou {jogador} e a cpu jogou {cpu}. Total de {soma} DEU ({ 'PAR' if soma % 2 == 0 else 'ÍMPAR'})}}")
    print(f"{25 * '--'}")
    if jogo == 'P' and soma % 2 == 1:
        print("Perdeu")
        print(f"{25 * '-='}")
        break
    elif jogo == 'I' and soma % 2 == 2:
        print("Perdeu")
        print(f"{25 * '-='}")
        break
    else:
        print("Venceu")
        vitoria += 1
        print(f"{25 * '-='}")

print(f"Você venceu {vitoria} vezes!")
