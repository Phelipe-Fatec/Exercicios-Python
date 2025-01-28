def dobro(n=0):
    dobro = n * 2
    return dobro


def metade(n=0):
    metade = n / 2
    return metade


def aumentar(n=0, taxaMais=0):
    aumenta = n + (n * (taxaMais / 100))
    return aumenta


def diminuir(n=0, taxaMenos=0):
    diminui = n - (n * (taxaMenos / 100))
    return diminui

def moeda(n=0, moeda='R$'):
    return f'{moeda} {float(n)}'.replace('.', ',')

def resumo(n=0,taxaMais=0, taxaMenos=0):
    print('=' * 30)
    print("Resumo do valor".center(30))
    print('=' * 30)
    print(f"Preço analisado: \tR$ {n}")
    print(f"Dobro do preço: \t{moeda(dobro(n))}")
    print(f"Metade do preço: \t{moeda(metade(n))}")
    print(f"{taxaMais}% de aumento:  \t{moeda(aumentar(n, taxaMais))}")
    print(f"{taxaMenos}% de redução:  \t{moeda(diminuir(n, taxaMenos))}")
    print('=' * 30)