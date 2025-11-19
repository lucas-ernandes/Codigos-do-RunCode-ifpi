def data_formatada(dia_1, mes_1, ano_1, dia_2, mes_2, ano_2):
    if ano_1 > ano_2:
        print(f'{dia_1}/{mes_1}/{ano_1}')
    elif ano_1 <  ano_2:
        print(f'{dia_2}/{mes_2}/{ano_2}')
    else:
        if mes_1 > mes_2:
            print(f'{dia_1}/{mes_1}/{ano_1}')
        elif mes_1 < mes_2:
            print(f'{dia_2}/{mes_2}/{ano_2}')
        else:
            if dia_1 > dia_2:
                print(f'{dia_1}/{mes_1}/{ano_1}')
            elif dia_1 < dia_2:
                print(f'{dia_2}/{mes_2}/{ano_2}')
            else:
                print(f'{dia_1}/{mes_1}/{ano_1}')
def main():
    dia = int(input('Dia: '))
    mes = int(input('Mês: '))
    ano = int(input('Ano: '))
    print('Segunda data:')
    dia_1 = int(input('Dia: '))
    mes_1 = int(input('Mês: '))
    ano_1 = int(input('Ano: '))
    
    data_formatada(dia, mes, ano, dia_1, mes_1, ano_1)
if __name__=='__main__':
    main()