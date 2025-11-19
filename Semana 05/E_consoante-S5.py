# Processamento de Dados
def letras(caracter):
    # retorna todo o alfabeto
    car = caracter.lower()
    return len(car) == 1 and car.isalpha() and car not in 'AEIOUaeiou'

# Programa principal

def main():
#Entrada
    l = input('Digite um caractere: ')
    print(f'Seu caractere é: {letras(l)}')

#Saida
if __name__ == '__main__':
    main()