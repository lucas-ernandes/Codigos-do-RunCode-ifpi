def qtd_pares(numero):
# Converte o número para string para poder percorrer dígito por dígito
    digitos = str(numero)
 #Inicializa o contador de dígitos pares
    impar = 0
# -Para- cada caractere (dígito) na string
    for d in digitos:
        if int(d) % 2 != 0:
            impar += 1
    return impar
#Processo de Dados
def main():
    impa = int(input('Insira um número de 10 até 99: '))
    #Condições
    if qtd_pares(impa) == 1:
        print('Apenas um dígito é ímpar.')
    elif qtd_pares(impa) == 0:
        print('Nenhum dígito é ímpar.')
    else:
        print('Os dois dígitos são ímpares.')
        
if __name__=='__main__':
    main()