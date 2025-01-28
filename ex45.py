from datetime import date
def votar(a=0):
    ano = date.today().year
    idade = ano - a
    if idade >= 18:
        return f"{idade} anos = Voto obrigatório"

    elif idade < 18 and idade >= 16:

        return f"{idade} anos = Voto opcional"
    else:
        return f"{idade} anos = Não pode votar"


nascimento = int(input("Digite o ano de nascimento: "))
print(votar(nascimento))