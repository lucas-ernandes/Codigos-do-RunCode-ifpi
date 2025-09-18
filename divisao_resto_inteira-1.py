dividendo = float(input('Dividendo: ').strip())
divisor = float(input('Divisor: ').strip())
calculo_1 = dividendo // divisor
calculo_resto = dividendo % divisor
print(f'= {calculo_1:.4f}')
print(f'{calculo_resto:.4f}')
