i = 1  # Contador para numerar os casos (Case 1, Case 2, ...)

while True:
    entrada = input()  # Lê uma linha da entrada
    if entrada == "0 0":  # Condição de parada: quando encontrar "0 0"
        break
    
    R, N = map(int, entrada.split())  # Separa a entrada em dois inteiros: R (ruas), N (números alocados)

    D = -1  # Inicializa D como -1 (valor inválido), será atualizado se encontrarmos uma solução válida
    
    # Verifica para cada valor possível de sufixo D (de 0 a 26)
    for d in range(27):  # d representa a quantidade de sufixos diferentes usados (0 a 26)
        if N * (1 + d) >= R:  # Verifica se é possível nomear todas as ruas com N números e d sufixos
            D = d  # Se sim, armazenamos esse valor como o mínimo necessário
            break  # Paramos o loop, pois já encontramos o menor D possível

    # Se D não foi alterado, significa que mesmo com 26 sufixos não é possível nomear todas as ruas
    if D == -1:
        print(f"Case {i}: impossible")  # Imprime "impossible" no formato pedido
    else:
        print(f"Case {i}: {D}")  # Caso contrário, imprime o número mínimo de sufixos necessários

    i += 1  # Incrementa o número do caso para a próxima linha de entrada
