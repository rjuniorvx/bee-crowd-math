import sys
import math  # usado para calcular a hipotenusa com math.hypot()

# Lê todas as linhas da entrada padrão até EOF
for linha in sys.stdin:
    # Remove espaços e quebras de linha e ignora linhas vazias
    if not linha.strip():
        continue

    # Separa os valores da linha e converte para inteiros
    D, VF, VG = map(int, linha.strip().split())

    # Distância que o ladrão percorre para alcançar águas internacionais
    distancia_fugitivo = 12  # sempre 12 milhas náuticas

    # Calcula o tempo que o ladrão leva: tempo = distância / velocidade
    tempo_fugitivo = distancia_fugitivo / VF

    # A Guarda Costeira parte de um ponto a D milhas ao longo da costa
    # e precisa alcançar o ponto no mar onde o ladrão estará (12 milhas mar adentro)
    # Isso forma um triângulo, e a guarda percorre a hipotenusa
    distancia_guarda = math.hypot(D, 12)  # sqrt(D² + 12²)

    # Calcula o tempo que a guarda leva: 'tempo = distância / velocidade'
    tempo_guarda = distancia_guarda / VG

    # Compara os tempos: se a guarda chega antes ou ao mesmo tempo, ela consegue interceptar
    if tempo_guarda <= tempo_fugitivo:
        print('S')  # Guarda consegue alcançar o ladrão
    else:
        print('N')  # Ladrão escapa antes de ser interceptado
