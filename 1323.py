import sys

# Lê cada linha da entrada até encontrar um zero
for linha in sys.stdin:
    N = int(linha.strip())
    if N == 0:
        break 
        
    total_quadrados = 0

    # Para cada tamanho de quadrado k x k, de 1 até N
    for k in range(1, N + 1):
        # Em um tabuleiro N x N, cabem (N - k + 1) quadrados por linha e coluna
        total_quadrados += (N - k + 1) ** 2

    print(total_quadrados)