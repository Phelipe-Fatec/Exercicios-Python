lista = []
pessoas = []
pmaior = []
pmenor = []
maior = 0
menor = 0
while True:
    lista.append(str(input("Digite o nome: ")))
    lista.append(float(input("Digite o peso: ")))
    if len(pessoas) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    pessoas.append(lista[:])
    lista.clear()
    resp = str(input("Deseja continuar? [S / N]: ")).upper().strip()
    while resp not in 'SsNn':
        print("inválido")
        resp = str(input("Deseja continuar? [S / N]: ")).upper().strip()
    if resp in 'Nn':
        break


print(pessoas)
print(f"{len(pessoas)} pessoas foram digitadas!")
print(f"O maior peso foi {maior}! \nPessoas com esse peso: ", end='')
for i, pessoa in enumerate(pessoas):
    if pessoa[1] == maior:
        print(f"{pessoa[0]}... ", end='')
print('')
print(f"O menor peso foi {menor}! \nPessoas com esse peso: ", end='')
for i, pessoa in enumerate(pessoas):
    if pessoa[1] == menor:
        print(f"{pessoa[0]}... ", end='')