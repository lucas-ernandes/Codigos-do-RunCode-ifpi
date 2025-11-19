def horas(minutos_total):
    minuto_calcu = minutos_total // 60
    calculo = minutos_total % 60
    return f'{minuto_calcu}H:{calculo}min'
def main():
    qtd_min = int(input('Quantos minutos deseja converter: '))
    print(f'{qtd_min} minutos vai dá {horas(qtd_min)}')
    
if __name__ == '__main__':
    main()