sexo = str(input("Por favor informe seu sexo [M/F]")).upper()
if sexo == 'F' or sexo == 'M':
    print(f"Sexo {sexo} registrado!")
else:
    while sexo != 'M' or sexo != 'F':
        invalido = str(input("Dados inválidos. Por favor informe seu sexo [M/F]: ")).upper()
        if invalido == 'F' or invalido == 'M':
            print(f"Sexo {invalido} registrado!")
            break



