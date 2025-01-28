n50 = 0
n20 = 0
n10 = 0
n1 = 0
valor = int(input("Qual valor você quer sacar? "))

while True:
    if valor > 50:
        valor =- 50
        n50 =+ 1
    elif valor > 20:
        valor -= 20
        n20 += 1
    elif valor > 10:
        valor -= 10
        n10 += 1
    elif valor > 1:
        valor -=10
        n1 +=1
    if valor == 0:
        break
print(f"notas de 50: {n50}")
print(f"notas de 20: {n20}")
print(f"notas de 10: {n10}")
print(f"notas de 1: {n1}")