pessoas = []
idades = []
mulheres = []
while True:
    pess = {}
    pess['nome'] = str(input("Nome: "))
    pess['sexo'] = str(input("Sexo [M/F]: ")).strip().upper()
    while pess['sexo'] not in 'MmFf':
        print('Inválido')
        pess['sexo'] = str(input("Sexo [M/F]: ")).strip().upper()
    if pess['sexo'] in 'Ff':
        mulheres.append(pess['nome'])
    pess['idade'] = int(input("Idade: "))
    idades.append(pess['idade'])
    pessoas.append(pess)
    continuar = str(input("Quer continuar [S/N]: ")).strip().upper()
    while continuar not in 'SsNn':
        print('Inválido')
        continuar = str(input("Quer continuar [S/N]: ")).strip().upper()
    if continuar in 'Nn':
        break

media = sum(idades) / len(idades)
print('=-' * 30)
print(pessoas)
print(idades)
print(mulheres)
print('=-' * 30)

print(f"A) Ao todo {len(pessoas)} pessoas foram cadastradas")
print(f"B) A média de idade é de {media} anos.")
print(f"C) As mulheres cadastradas foram: ", end='')
for k, v in enumerate(mulheres):
    print(v, end=' ')
print()
print(f"D) As pessoas com idade acima da média são: ")
for p in pessoas:
    if p['idade'] > media:
        for k, v in p.items():
            print(f"{k} = {v}; ", end='')
        print()

