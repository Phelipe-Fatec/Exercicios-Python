lista = []
dig = 0
cinco = 0
while True:
    n = int(input("Digite um número: "))
    lista.append(n)
    if n == 5:
        cinco += 1
    dig += 1
    perg = str(input("Deseja continuar? [S \ N]: ")).strip().lower()
    while perg not in 'SsNn':
        print("Inválido")
        perg = str(input("Deseja continuar? [S \ N]: ")).strip().lower()
    if perg in 'Nn':
        break
print(f"Lista em ordem crescente: {lista}")
lista.sort(reverse=True)
print(f"Lista em ordem descrescente: {lista}")
print(f"A lista tem {dig} digitos")
if cinco > 0:
    print(f"Número cinco digitado {cinco} vezes.")
else:
    print(f"Número cinco não foi digitado")
