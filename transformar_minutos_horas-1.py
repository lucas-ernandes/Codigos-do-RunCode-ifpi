#variavel 'minutos' recebe convertido em inteiro, e lido pelo o usuario
minutos = int(input('Quantidades minutos: ').strip())
#variavel 'tempo' recebe calculo de minutos dividindo por 60
tempo = minutos // 60
#variavel 'temp_2' recebe calculo de resto 
temp_2 = minutos % 60
#imprime na tela o resultado da divisao e o resto, e mostra as horas e minutos
print(f'{tempo}h{temp_2}min')
