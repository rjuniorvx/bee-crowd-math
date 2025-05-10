i = int(input()) # Número de casos que serão testados

for _ in range(i):
  c = float(input()) # Quantidade inicial de comida
  dias = 0

  while c > 1.0:
    c = c / 2.0
    dias += 1 

  print(f"{dias} dias")