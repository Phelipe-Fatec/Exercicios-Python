import random
import time


def sorteiaLista(lista):
    for i in range(0, random.randint(0, 10)):
        lista.append(random.randint(0, 10))
    print("Sorteando valores da lista: ", end=' ')
    for i in lista:
        print(i, end=' ')
        time.sleep(0.5)
    print("Pronto!")
def somaPar(lista):
    par = 0
    for i in lista:
        if i % 2 == 0:
            par += i
    print(f"Somando os valores pares de {lista} teremos o número {par}")

lista = []
sorteiaLista(lista)
print()
somaPar(lista)
