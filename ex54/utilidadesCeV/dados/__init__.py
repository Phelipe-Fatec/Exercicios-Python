def lerDinheiro(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isalpha():
            print(f"ERRO: '{n}' não é um preço válido")
        else:
            valor = n
            ok = True
        if ok:
            break
    return float(valor)