matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
maiorl = somapar = somacol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um número para [{l}][{c}]: "))
print(matriz)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()
for l in range(0, 3):
    somacol += matriz[l][2]
for c in range(0,3):
    if matriz[1][c] == 0:
        maiorl = matriz[1][c]
    else:
        if matriz[1][c] > maiorl:
            maiorl = matriz[1][c]
print(somapar)
print(somacol)
print(maiorl)