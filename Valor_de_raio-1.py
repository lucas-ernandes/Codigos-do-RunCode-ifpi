PI = 3.141592
raio = float(input('Digite um raio: ').strip())
circuferencia = 2 * PI *raio
area_circulo = PI * raio**2
area_esfera = 4* PI * raio **2
vol_esfra = 4/3 * PI * raio **3
print(f'{circuferencia:.6f}')
print(f'{area_circulo:.6f}')
print(f'{area_esfera:.6f}')
print(f'{vol_esfra:.6f}')
