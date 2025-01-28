import time


'''def cont1():
    for contagem in range(0, 11, +1):
        print(contagem, end=' ')
        time.sleep(0.5)

def cont2():
    for contagem in range(10, -1, -2):
        print(contagem, end=' ')
        time.sleep(0.5)'''

def contP(inicio, fim, passo):
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    if inicio > fim:
        for contagem in range(inicio, fim - 1, passo):
            print(contagem, end=' ')
            time.sleep(0.5)
    elif inicio < fim:
        for contagem in range(inicio, fim + 1, passo):
            print(contagem, end=' ')
            time.sleep(0.5)

'''print("Contagem de 0 até 10 de 1 em 1:")
cont1()
time.sleep(0.5)
print()
print("Contagem de 10 até 0 de 2 em 2:")
cont2()
time.sleep(0.5)'''

print("Agora sua vez!")
i = int(input("Digite o ínicio da contagem: "))
f = int(input("Digite o fim da contagem:"))
p = int(input("Digite o passo da contagem: "))
contP(i, f, p)