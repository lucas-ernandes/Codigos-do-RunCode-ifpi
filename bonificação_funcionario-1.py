tempo_ano = int(input('Tempo em serviço: ').strip())
valor_de_bonus = float(input('Valor por ano: ').strip())
bonus = tempo_ano * valor_de_bonus
print('Bônus de %4.2f'%bonus)
