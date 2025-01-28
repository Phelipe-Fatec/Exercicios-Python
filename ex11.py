cont = 0
num = 0
soma = 0
while True:
    num = int(input("Digite um número [999 para parar]: "))
    if num == 999:
        break
    cont += 1
    soma += num
print(f"A soma dos {cont} valores é {soma} ")