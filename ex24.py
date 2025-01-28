'''
Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista.

Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

lista = []

while True:
    inserir = int(input("Insira um valor: "))
    if inserir in lista:
        print("Valor já está presente")
    else:
        lista.append(inserir)
    continuar = str(input("Deseja continuar? [S \ N] ")).lower().strip()
    while continuar not in 'SsNn':
        print('Inválid')
        continuar = str(input("Deseja continuar? [S \ N] ")).lower().strip()
    if continuar in 'Nn':
        break

lista.sort()
print(lista)
