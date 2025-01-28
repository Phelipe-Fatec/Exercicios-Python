tupla = []
cont = 0

nove = 0
tres = 0
pares = []
for n in range (0, 4):
    t = int(input(f"Digite o {n + 1}º número: "))
    tupla.append(t)
    if t == 9:
        nove += 1
    if t == 3:
        tres += 1
    if t % 2 == 0:
        pares.append(t)

print(tupla)

if nove > 1:
    print(f"Nove apareceu {nove} vezes")
elif nove == 1:
    print(f"Nove apareceu {nove} vez")
elif nove <= 0:
    print(f"Nove não apareceu")

if tres >= 1:
    print(f"Três apareceu na posição {tupla.index(3) + 1}")

print(f"Números pares foram {pares}")
