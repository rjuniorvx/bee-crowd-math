import sys
# Loop para ler cada linha da entrada até o fim (EOF)
for linha in sys.stdin:
    # Divide a linha em duas partes (por espaço) e converte ambas para inteiros
    # Exemplo: linha = "5 2" → ['5', '2'] → v = 5, t = 2
    v, t = map(int, linha.split())

    # Calcula e imprime o deslocamento no dobro do tempo: s = 2 * v * t
    print(2 * v * t)
