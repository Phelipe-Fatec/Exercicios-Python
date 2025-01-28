import random

#Minha versão abaixo
'''def descMaior():
    lista = []
    for i in range(0, random.randint(0, 10)):
        lista.append(random.randint(0, 10))
    print(lista, end=' ')
    print(f"Foram informados {len(lista)} valores ao todo")

    maior = 0
    for c in lista:
        if c > maior:
            maior = c
    print(f"O maior número foi {maior}")
    lista.clear()

descMaior()'''

#Versão 'Guanabára'
def maior(* num):
    print(num)

    maior = 0
    for c in num:
        if c > maior:
            maior = c
    print(f"O maior número foi {maior}")
maior(10, 15, 3, 6, 8, 4)