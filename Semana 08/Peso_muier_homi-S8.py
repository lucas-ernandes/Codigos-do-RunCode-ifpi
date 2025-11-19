def peso_ideal(altu, sexo):
    homi = (72.7 * altu) - 58
    muier = (62.1 * altu) - 44.7
    if sexo == 1:
        print(f'Para homens: {homi:.2f}')
    elif sexo == 2:
        print(f'Para mulheres: {muier:.2f}')
def main():
    altura = float(input('Sua altura(M): '))
    sexo = int(input('Sexo (1) macho ou (2) fêmea: '))
    peso_ideal(altura, sexo)
if __name__=='__main__':
    main()