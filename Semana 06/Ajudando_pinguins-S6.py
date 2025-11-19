def help_me(celsius):
    convercao = (celsius*(9/5))+32
    return convercao
def main():
    temperatura = float(input('Digite uma temperatura em Grauº Celsius: '))
    print(f'A temperatura {temperatura}ºC convertida em Fahrenheit é: {help_me(temperatura):.2f}º')
if __name__=='__main__':
    main()