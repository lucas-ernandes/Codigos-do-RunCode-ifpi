#Pergunte ao usuário quantos quilômetros até Marte e quantos quilômetros por hora sua nave espacial pode viajar. Calcule e mostre quanto tempo levaria para chegar a Marte.

marte = int(input('Quantos Km até marte: ').strip())
velocidade = int(input('Quantos sua nave pega: ').strip())
calculo = marte / velocidade
print(f' Sua nave levaria, {calculo} horas pra chegar em Marte')
