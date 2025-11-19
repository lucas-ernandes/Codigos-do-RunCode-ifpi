def valida_idade(data):
    # A data no formato DDMMAAAA

    dia = int(data[:2])
    mes = int(data[2:4])
    ano = int(data[4:])

    # Verifica se o mês é válido
    if not (1 <= mes <= 12):
        return False

    # Verifica se o ano é bissexto
    bissexto = ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)

    # Define o número de dias de cada mês
    if mes == 2:
        dias_no_mes = 29 if bissexto else 28
    elif mes in [4, 6, 9, 11]:
        dias_no_mes = 30
    else:
        dias_no_mes = 31

    # Verifica se o dia é válido
    return 1 <= dia <= dias_no_mes

def main():
    data = input('Digite uma data: ').strip()
    print('Se "true" ela é bissexto')
    print(valida_idade(data))
if __name__=='__main__':
    main()