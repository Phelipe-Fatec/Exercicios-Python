from datetime import datetime
pessoa = {}

pessoa['nome'] = str(input("Digite o nome da pessoa: "))
nasc = int(input("Digite o ano de nascimento: "))
pessoa['idade'] = datetime.now().year - nasc
pessoa['clt'] = int(input("Digite a carteira de trabalho (0 = não tem): "))

if pessoa['clt'] == 0:
    print('=-' * 30)
    for k, v in pessoa.items():
        print(f"{k}: {v}")
else:
    pessoa['contratacao'] = int(input("Digite o ano de contratação: "))
    pessoa['salario'] = int(input("Digite o salário: R$"))
    pessoa['aposentadoria'] = (pessoa['contratacao'] + 35) - nasc

    print('=-' * 30)
    for k, v in pessoa.items():
        print(f"{k}: {v}")