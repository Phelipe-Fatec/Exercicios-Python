def fatorial(n, show=False):
    """
    --> Calcula o fatorial de um número

    :param n: O número a ser calculado
    :param show: Se verdadeiro, irá mostrar a conta
    :return: Retorna o valor fatorial de n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            if c > 1:
                print(f'{c} X ', end='')
            elif c == 1:
                print(f'{c} = ', end='')
        f *= c
    return f



print(fatorial(5, show=True))
help(fatorial)