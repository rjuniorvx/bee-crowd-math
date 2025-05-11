import sys
# Loop que percorre cada linha da entrada padrão, até EOF
for linha in sys.stdin:
    # Remove espaços em branco do início e fim da linha, divide a linha em partes e converte cada parte em int
    hashmat, oponente = map(int, linha.strip().split())
    
    # Calcula e imprime a diferença absoluta entre os dois números
    print(abs(hashmat - oponente))
