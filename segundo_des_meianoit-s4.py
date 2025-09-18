hora = int(input('Quantas horas: ').strip())*60
minuto = int(input('Quantos minutos: ').strip())
segundo = int(input('Quantos segundos: ').strip())
tempo = hora * 60
tempo_2 = minuto * 60
calculo = tempo + tempo_2 + segundo
print('São', calculo, 'segundos desde as ultimas 00:00')