extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')

while True:
    núm = int(input("Digite um número de 0 à 20: "))
    if 0 <= núm <= 20:
        break
    print("Tente novamente. ", end='')
print(extenso[núm])