def dobro(n):
    dobro = n * 2
    return dobro


def metade(n):
    metade = n / 2
    return metade


def aumentar(n):
    aumenta = n + (n * 0.10)
    return aumenta


def diminuir(n):
    diminui = n - (n * 0.10)
    return diminui

def moeda(n=0, moeda='R$'):
    return f'{moeda} {float(n)}'.replace('.', ',')
