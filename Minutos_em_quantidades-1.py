segundo = int(input('Insira um número em segundos: ').strip())
minuto = segundo // 60
resto = segundo % 60
print(f'Dá {minuto} minuto...')
print(f'e {resto} segungos.')
