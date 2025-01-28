cont = 0
soma = 0
num = 0
while cont != 999:
    cont = int(input("Digite um número [999 para saír]: "))
    if cont != 999:
        soma = soma + cont
        num +=1
print(f"Você digitou {num} números, e a soma de todos eles é {soma}")