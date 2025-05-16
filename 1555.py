# Lê o número de rodadas (partidas) que o jogo terá
i = int(input())

# Laço para repetir o jogo para cada rodada
for _ in range(i):
    # Lê os valores de x e y para cada rodada
    x, y = map(int, input().split())
    
    # Calcula o valor de r para Rafael
    r = ((3*x)**2) + y**2
    
    # Calcula o valor de b para Beto
    b = 2*(x**2) + ((5*y)**2)
    
    # Calcula o valor de c para Carlos
    c = -100 * x + y ** 3

    # Verifica quem tem o maior valor e declara o vencedor
    if r > b and r > c:
        # Se o valor de r for maior que b e c, Rafael ganha
        print("Rafael ganhou")
    elif b > r and b > c:
        # Se o valor de b for maior que r e c, Beto ganha
        print("Beto ganhou")
    else:
        # Caso contrário, Carlos ganha
        print("Carlos ganhou")
