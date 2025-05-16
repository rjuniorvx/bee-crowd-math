import math

while True:
    try:
        a, b, c = map(float, input().split())
        p = (a + b + c) / 2

        # Área do triângulo (Heron)
        area_triangulo = math.sqrt(p * (p - a) * (p - b) * (p - c))

        # Área do círculo inscrito (rosas vermelhas)
        r_incirculo = area_triangulo / p
        area_incirculo = math.pi * r_incirculo ** 2

        # Área do círculo circunscrito (girassóis amarelos)
        r_circuncirculo = (a * b * c) / (4 * area_triangulo)
        area_circuncirculo = math.pi * r_circuncirculo ** 2

        # Violetas azuis
        area_azul = area_triangulo - area_incirculo

        # Girassóis amarelos
        area_amarela = area_circuncirculo - area_triangulo

        print(f"{area_amarela:.4f} {area_azul:.4f} {area_incirculo:.4f}")

    except EOFError:
        break

