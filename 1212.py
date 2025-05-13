# Loop principal que continua até receber a entrada "0 0"
while True:
    a, b = input().split()  # Lê dois números como strings, separados por espaço
    if a == "0" and b == "0":
        break

    a = a.zfill(10)  # Preenche a string 'a' com zeros à esquerda até ter 10 caracteres
    b = b.zfill(10)  # Faz o mesmo para 'b'

    carry = 0         # Variável para armazenar se há um "vai 1" (carry) da operação anterior
    carry_count = 0   # Contador de quantas vezes ocorreu um "leva 1"

    # Percorre os dígitos de ambos os números da direita para a esquerda
    for i in range(9, -1, -1):  # Começa do último índice (posição 9) até a posição 0
        soma = int(a[i]) + int(b[i]) + carry  # Soma os dígitos correspondentes mais o carry anterior
        if soma >= 10:       # Se a soma for 10 ou mais, há um carry
            carry = 1        # Define carry para 1 para a próxima posição à esquerda
            carry_count += 1 # Incrementa o contador de carry
        else:
            carry = 0        # Se a soma for menor que 10, zera o carry

    # Impressão da saída com base na quantidade de operações "leva 1"
    if carry_count == 0:
        print("No carry operation.")  # Nenhum carry
    elif carry_count == 1:
        print("1 carry operation.")   # Um carry
    else:
        print(f"{carry_count} carry operations.")  # Mais de um carry
