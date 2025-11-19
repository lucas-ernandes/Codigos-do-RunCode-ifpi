def inverter_num(valor):
    return str(valor) [::-1]

def main():
    num = int(input('Digite um número de 1000 a 9999: '))
    print(f'Seu numero invertido é: {inverter_num(num)}')

if __name__ == '__main__':
    main()