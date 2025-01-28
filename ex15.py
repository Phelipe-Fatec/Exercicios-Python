aux = 0
aux2 = 0
aux3 = 0
aux4 = 0
aux5 = ''
while True:
    prod = str(input("Digite o nome do produto: "))
    preco = int(input("Digite o preço do produto: "))
    resp = ' '
    aux3 =+ 1
    aux2 += preco
    if aux3 == 1 or preco < aux4:
        aux5 = prod
    if preco > 1000:
        aux += 1
    while resp not in 'SN':
        resp = str(input("Quer continuar? [S/N]")).upper().strip()[0]
    if resp == 'N':
        break
print(f"Produtos acima de mil: {aux}")
print(f"Total: {aux2}")
print(f"Mais barato: {aux5}")