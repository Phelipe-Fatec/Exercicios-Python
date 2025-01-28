import time

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = num1 + num2
multi = num1 * num2
maior = 0
if num1 > num2:
    maior = num1
elif num2 > num1:
    maior = num2
print("[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] novos números\n[ 5 ] sair")
menu = str(input("Qual sua opção: "))
while menu != '5':
    if menu == '1':
        print(f"A soma entre {num1} e {num2} é {soma}!")
        time.sleep(0.5)
        print("[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] novos números\n[ 5 ] sair")
        menu = str(input("Qual sua opção: "))
    elif menu == '2':
        print(f"A multiplicação entre {num1} e {num2} é {multi}!")
        time.sleep(0.5)
        print("[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] novos números\n[ 5 ] sair")
        menu = str(input("Qual sua opção: "))
    elif menu == '3':
        if num1 == num2:
            print(f"Os números são iguais")
        else:
            print(f"O maior número é {maior}")
        time.sleep(0.5)
        print("[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] novos números\n[ 5 ] sair")
        menu = str(input("Qual sua opção: "))
    elif menu == '4':
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        soma = num1 + num2
        multi = num1 * num2
        maior = 0
        if num1 > num2:
            maior = num1
        elif num2 > num1:
            maior = num2
        print("[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] novos números\n[ 5 ] sair")
        menu = str(input("Qual sua opção: "))
        time.sleep(0.5)
    elif menu not in '12345':
        print(f"Opção inválida!")
        time.sleep(0.5)
        print("[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] novos números\n[ 5 ] sair")
        menu = str(input("Qual sua opção: "))

print("Finalizando...")
time.sleep(1)

