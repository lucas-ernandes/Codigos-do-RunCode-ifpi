def IMC(n1, n2):
    calculo = n1 / (n2**2)
    print(f'Seu IMC: {calculo:.2f}')
    if calculo < 18.5:
        print('Abaixo do peso')
    elif calculo < 25:
        print('Peso normal')
    elif calculo < 30:
        print('Sobrepeso')
    elif calculo < 35:
        print('Obeso leve')
    elif calculo < 40:
        print('Obeso moderado')
    else:
        print('Obeso mórbido')
def main():
    peso = float(input('Seu peso(kg): '))
    altura = float(input('Sua altura(m): '))
    IMC(peso, altura)
if __name__=='__main__':
    main()