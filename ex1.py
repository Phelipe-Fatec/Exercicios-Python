import datetime
ano = 2023
totmaior = 0
totmenor = 0

for pessoa in range (1, 8):
    idade = int(input(f"Digite o ano de nascimento da {pessoa}ª pessoa: "))
    total = ano - idade
    if total < 21:
        totmenor += 1
    else:
        totmaior += 1

print(f"{totmaior} são maiores de idade")
print(f"{totmenor} são menores de idade")
