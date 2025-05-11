N = int(input())  # Número de casos de teste

for i in range(1, N + 1):
    entrada = input().split()  # Lê a entrada e separa valor e formato
    X = entrada[0]
    formato = entrada[1]

    print(f"Case {i}:")
    
    if formato == "bin":
        decimal = int(X, 2)  # Converte de binário para decimal
        print(f"{decimal} dec")
        print(f"{hex(decimal)[2:]} hex")  # Hex sem '0x'

    elif formato == "dec":
        decimal = int(X)  # Já está em decimal
        print(f"{hex(decimal)[2:]} hex")  # Hex sem '0x'
        print(f"{bin(decimal)[2:]} bin")  # Bin sem '0b'

    elif formato == "hex":
        decimal = int(X, 16)  # Converte de hexadecimal para decimal
        print(f"{decimal} dec")
        print(f"{bin(decimal)[2:]} bin")  # Bin sem '0b'

    print()  # Linha em branco após cada caso
