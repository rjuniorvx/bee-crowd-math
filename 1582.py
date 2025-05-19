import sys
from math import gcd  # Importa a função gcd (máximo divisor comum) da biblioteca math

# Loop para ler cada linha da entrada até EOF
for linha in sys.stdin:
    partes = linha.strip().split()  # Remove espaços extras e divide a linha em partes
    if len(partes) != 3:            # Garante que há exatamente 3 valores na linha
        continue                    # Se não houver, ignora a linha e continua

    x, y, z = map(int, partes)      # Converte as 3 partes para inteiros
    a, b, c = sorted([x, y, z])     # Ordena os valores para garantir que c seja o maior (hipotenusa)

    # Verifica se a tripla satisfaz o Teorema de Pitágoras: a² + b² == c²
    if a**2 + b**2 == c**2:
        # Calcula o máximo divisor comum dos três números
        mdc_total = gcd(gcd(a, b), c)

        # Se o mdc for 1, é uma tripla pitagórica primitiva
        if mdc_total == 1:
            print("tripla pitagorica primitiva")
        else:
            # É uma tripla pitagórica, mas não primitiva
            print("tripla pitagorica")
    else:
        # Não satisfaz o teorema, portanto não é uma tripla pitagórica
        print("tripla")
