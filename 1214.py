c = int(input())

# Loop que será executado c vezes (uma vez para cada caso de teste)
for _ in range(c):
    # Lê a linha do caso de teste, separa os valores e armazena na lista 'entrada'
    entrada = input().split()

    # O primeiro valor da entrada é o número de estudantes da turma
    n = int(entrada[0])

    # Os demais valores são as notas dos estudantes
    notas = list(map(int, entrada[1:]))

    # Inicializa a variável 'soma' para calcular a soma das notas
    soma = 0
    for nota in notas:
        soma += nota  # Soma todas as notas da turma

    # Calcula a média da turma
    media = soma / n

    # Conta quantos estudantes têm nota acima da média
    acima_da_media = 0
    for nota in notas:
        if nota > media:
            acima_da_media += 1

    # Calcula o percentual de estudantes acima da média
    percentual = (acima_da_media / n) * 100

    # Imprime o percentual com 3 casas decimais, seguido de '%' como especificado
    print(f"{percentual:.3f}%")
