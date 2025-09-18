distancia = int(input('Qual a distancia até o seu planeta: ').strip())
velocidade = int(input('Qual a velocidade de sua nave: ').strip())
tempo = distancia // velocidade
calculo = tempo // 24
print(f"{calculo} dias e {tempo - (calculo*24)} horas")
