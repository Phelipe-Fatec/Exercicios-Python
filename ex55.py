def lerint(msg):
    valor = 0
    n = str(input(msg))
    if n.isnumeric():
         n
    else:
        try:
           n.isnumeric()
        except:
            print("Erro! Digite um número inteiro válido")



n = lerint("Digite um número: ")
print(f"Você digitou o número {n}")