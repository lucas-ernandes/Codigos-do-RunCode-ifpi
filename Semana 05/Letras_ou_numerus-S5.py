# Processamento de Dados
def letras(caracter):
    #Retorna apenas letras e numeros
    return caracter.isalnum()

# Programa principal

def main():
#Entrada
    l = input('Digite um caractere: ')
    print(f'Seu caractere é: {letras(l)}')

#Saida
if __name__ == '__main__':
    main()