def dobro(n = 0, formato=False):
    dobro = n * 2
    return dobro if not formato else moeda(dobro)


def metade(n = 0, formato=False):
    metade = n / 2
    return metade  if not formato else moeda(int(metade))


def aumentar(n=0, taxa=0, formato=False):
    aumenta = n + (n * (taxa / 100))
    return aumenta if not formato else moeda(int(aumenta))


def diminuir(n=0, taxa=0, formato=False):
    diminui = n - (n * (taxa / 100))
    return diminui if not formato else moeda(int(diminui))

def moeda(n=0, moeda='R$'):
    return f'{moeda} {float(n)}'.replace('.', ',')
