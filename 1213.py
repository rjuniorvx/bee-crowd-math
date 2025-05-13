import sys

for linha in sys.stdin:
    # Remove espaços em branco da linha e converte para inteiro
    n = int(linha.strip())

    count = 1  # Contador de quantos dígitos '1' foram usados
    num = 1 % n  # Começa com o número 1 e calcula o resto da divisão por n

    # Enquanto o número formado por 'count' uns não for divisível por n
    while num != 0:
        # Gera o próximo número com mais um dígito '1' à direita
        # Ex: se num = 1, vira 11; se num = 11, vira 111, etc.
        # Calcula o novo resto da divisão por n
        num = (num * 10 + 1) % n
        count += 1  # Incrementa o número de dígitos usados

    # Quando o número formado por 'count' uns for divisível por n, imprime o count
    print(count)
