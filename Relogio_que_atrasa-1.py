#Você já se perguntou como seria um relógio que atrasa 3 minutos a cada hora? Vamos modelar isso com programação! Peça ao usuário para inserir o número de horas. Calcule e imprima o tempo que um relógio que atrasa 3 minutos por hora estaria atrás.

hora = int(input('Insira suas Horas: ').strip())
relogio = hora * 3
print(f'Seu relógio de 3 min atrasado ficou: {relogio}')
