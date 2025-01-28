tab = 0
cont = 0
multi = 0
while True:
    tab = int(input("Quer ver a tabuada de qual valor? "))
    if tab < 0:
        break
    for i in range(1, 11):
        cont += 1
        print(f"{tab} X {cont} = {tab * cont}")
    cont = 0