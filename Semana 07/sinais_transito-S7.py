def transito_strans(sinal):
    return sinal


def main():
    sinal_1 = input('Insira uma letra que presenta uma cor (V-verde, A-amarelo, E-Vermelho: )').upper()
    if sinal_1 == 'V':
        print('Sua cor inserida significa "Siga" no trânsito.')
    if sinal_1 == 'A':
        print('Sua cor inserida significa "Atenção" no trânsito.')
    if sinal_1 == 'E':
        print('Sua cor inserida significa "Pare" no trânsito.')


if __name__ == '__main__':
    main()
