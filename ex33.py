alunos = []

while True:
    nome = str(input("Digite o nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    resp = str(input("Deseja continuar? [S/N]: ")).upper().strip()
    while resp not in 'SsNn':
        print('Inválido')
        resp = str(input("Deseja continuar? [S/N]: ")).upper().strip()
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"Id.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, c in enumerate(alunos):
    print(f"{i:<4}{c[0]:<10}{c[2]:>8}")

while True:
    print('=-' * 30)
    opc = int(input("Deseja ver qual aluno? (Digite o Id, ou 999 para finalizar): "))
    if opc == 999:
        break
    print(f"Notas de {alunos[opc][0]} são {alunos[opc][1]}")