aluno = {}

aluno['Nome'] =  str(input("Digite o nome do aluno: "))
aluno['Media'] = float(input(f"Digite a média de {aluno['Nome']}: "))

if aluno['Media'] < 7:
    aluno['Situação'] = 'Reprovado'
elif aluno['Media'] >= 7:
    aluno['Situaçao'] = 'Aprovado'

for x, i in aluno.items():
    print(f"{x} é igual a {i}")