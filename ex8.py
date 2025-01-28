termo = int(input("Quantos termos mostrar? "))
t1 = 0
t2 = 1
contar = 3
print(t1)
print(t2)
while contar <= termo:
    t3 = t1 + t2
    print(f"{t3}")
    t1 = t2
    t2 = t3
    contar += 1