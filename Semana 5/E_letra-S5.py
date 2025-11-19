# Processamento de Dados
def letras(caracter):
    # retorna todo o alfabeto
    return caracter.isalpha()

# Programa principal

def main():
#Entrada
    l = input('Digite um caractere: ')
    print(f'Seu caractere é: {letras(l)}')

#Saida
if __name__ == '__main__':
    main()
