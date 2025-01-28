num = 0
letra = ''
atual = 0
maior = 0
menor = 0
cont = 0
soma = 0
while letra != 'n':
    atual = num
    num = int(input("Digite um número: "))
    cont += 1
    soma += num
    if num > atual:
        maior = num
    elif num < atual:
        menor = num
    letra = str(input("Quer continuar? [S/N]: ")).lower()

print(f"Você digitou {cont} números e a média foi {soma / cont}")
print(f"O maior numero digitado foi {maior}")
print(f"O menor número digitado foi {menor}")