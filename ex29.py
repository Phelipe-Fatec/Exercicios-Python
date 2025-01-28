lista = [[], []]
for i in range(0, 7):
    num = int(input(f"Digite o {i + 1}º número: "))
    if num % 2 == 0:
        lista[1].append(num)
    else:
        lista[0].append(num)
lista[0].sort()
print(lista[0])
lista[1].sort()
print(lista[1])