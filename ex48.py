def lerint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = n
            ok = True
        else:
            print("Erro! Digite um número inteiro válido")
        if ok:
            break
    return int(valor)


n = lerint("Digite um número: ")
print(f"Você digitou o número {n}")