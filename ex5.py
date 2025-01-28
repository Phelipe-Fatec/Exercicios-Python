import random

cpu = random.randint(1, 10)

jogador = int(input("Digite um número de 1 à 10: "))
tentativas = 1
while jogador != cpu:
    if jogador > cpu:
        print("Menos que isso...")
    elif jogador < cpu:
        print("Mais que isso")
    jogador = int(input("Digite um número de 1 à 10: "))
    tentativas += 1

print(f"Acertou com {tentativas} tentativas.\nCPU : {cpu}")