n = int(input())

for _ in range(n):
  x = int(input()) # Número estabelecido de CASAS
  total_graos = 1 # Inicia com 1 grão na primeira casa

  i = 1
  while i < x:
    total_graos  = total_graos * 2 + 1
    i += 1

  kg = total_graos // 12000
  print(f"{kg} kg")
