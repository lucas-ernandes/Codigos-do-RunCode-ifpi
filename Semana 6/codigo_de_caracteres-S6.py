#Definindo função que recebe(numero)
def numero_letra(numero):
    #Retorna o parametro(numero) em valor numerico
    return ord(numero) 
#Processamento de dados
def main():
    codigo = input('Digite uma letra: ')
    
    print(f'O caractere {codigo} em valor numerico é {numero_letra(codigo)}!')
    #Saida de dados
if __name__ == '__main__':
    main()