'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''

lista = []
listapar = []
listaimpar = []

while True:
    n = int(input("Digite um número: "))
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    perg = str(input("Deseja continuar? [S \ N]: ")).strip().lower()
    while perg not in 'SsNn':
        print("Inválido")
        perg = str(input("Deseja continuar? [S \ N]: ")).strip().lower()
    if perg in 'Nn':
        break
print(lista)
print(listapar)
print(listaimpar)