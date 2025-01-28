'''
Faça um programa que leia 5 valores números e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitados
e as suas respectivas posições na lista.
'''
lista = []
menorpos = []
maiorpos = []
for l in range(0, 5):
    lista.append(int(input(f"Digite o {l + 1}º número: ")))
print(lista)

menor = min(lista)
maior = max(lista)

for i, men in enumerate(lista):
    if men == menor:
        menorpos.append(i)

for i, mai in enumerate(lista):
    if mai == maior:
        maiorpos.append(i)

print(f"O menor número foi {menor} e ele apareceu nas posições: {menorpos}")
print(f"O maior número foi {maior} e ele apareceu nas posições: {maiorpos}")