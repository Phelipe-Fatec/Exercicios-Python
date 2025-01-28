palavras = ('aprender', 'programar', 'linguagem', 'python')

for p in palavras:
    print(f"\n A palavra {p.upper()} tem as vogais: ", end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')