idade = 0
maior = 0
masc = 0
femenor = 0
while True:
    print(f"{50 * '-'}")
    print("Cadastre uma pessoa")
    print(f"{50 * '-'}")
    sexo = ' '
    idade = int(input("Idade: "))
    while sexo not in 'MF':
        sexo = str(input("Sexo: [M/F] ")).upper().strip()[0]
    if idade > 18:
        maior += 1
    if sexo == 'M':
        masc += 1
    if sexo == 'F' and idade < 20:
        femenor += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if continuar == 'N':
        break
print(f"Total de pessoas com mais de 18: {maior}")
print(f"Total de homens cadastrados: {masc}")
print(f"Total de mulheres com menos de 20 anos: {femenor}")


