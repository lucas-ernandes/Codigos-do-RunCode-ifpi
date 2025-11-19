def lado_quadra(lado):
    return lado**2, lado*4

a = float(input('Lado do quadrado: ').strip())
area, perimetro = lado_quadra(a)
print(f"Area: {area:10.4f}")
print(f"Perimetro: {perimetro:10.4f}")