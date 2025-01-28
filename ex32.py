import random
import time
lista = []
num = int(input("Digite a quantidade de palpites: "))
aux = 0
while aux < num:
    for c in range(0, 6):
        x = random.randint(1, 60)
        if x not in lista:
            lista.append(x)
    lista.sort()
    print(lista)
    time.sleep(0.7)
    lista.clear()
    aux += 1