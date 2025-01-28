temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
awnser = []
contador = soma = 0
atual = -1
while True:
    print(temperatures[atual])

    if contador == len(temperatures):
        break
    contador += 1
    atual += 1

    # while temperatures[atual] <= temperatures[soma]:
    #
    #  if temperatures[soma] > temperatures[atual]:
    #     break

    #    soma += 1
    #   awnser.append(soma)

print(atual)
print(temperatures)
print(awnser)