import re
import sys

def gerarPalavras(texto):
    # Encontra palavras alfabéticas (ignorando caracteres especiais e números)
    return sorted(set(re.findall(r'\b[a-zA-Z]+\b', texto.lower())))

# Lê múltiplas linhas de entrada até EOF
print("Digite o texto (pressione Ctrl+D para finalizar no Linux/Mac ou Ctrl+Z no Windows):")
texto = sys.stdin.read()

# Gera e imprime as palavras
for palavra in gerarPalavras(texto):
    print(palavra)