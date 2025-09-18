altura = int(input('Altura: ').strip())
comprimento = int(input('Comprimento: ').strip())
largura = int(input('Largura: ').strip())
area_piso = largura*comprimento
volume = largura*comprimento*altura
area_parede = 2*altura*largura +2*altura*comprimento
print('A área do piso é:', area_piso)
print('Volume da sala:', volume)
print('Área da parede:', area_parede)