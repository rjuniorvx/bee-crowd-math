# Lê o número de casos de teste (um número inteiro)
N = int(input())

# Executa um laço para ler e processar cada caso de teste
for _ in range(N):
    # Lê uma linha contendo dois números inteiros A e B separados por espaço
    # Utilizamos input().split() para separar os valores e armazenar como strings
    A, B = input().split()
    
    # Verifica se a string B está no final da string A
    # Isso responde à pergunta: "B corresponde aos últimos dígitos de A?"
    if A.endswith(B):
        # Se sim, imprimimos "encaixa"
        print("encaixa")
    else:
        # Caso contrário, imprimimos "nao encaixa"
        print("nao encaixa")