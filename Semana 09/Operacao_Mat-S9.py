def matematica(n1, n2, Ope):
    print(n1 + n2 if Ope == 1 else
    (n1 - n2) if Ope == 2 else
    (n1 * n2) if Ope == 3 else
    (f'{n1 / n2:.2f}') if Ope == 4 else 'Complete a operação')
    
def main():
    print('Crie uma operação aritimetica')
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número para continuar a operação: '))
    operacao = int(input('Qual operação = 1- Adição; 2- Subtração; 3- Multiplicação; 4- Divisã:  '))
    matematica(n1, n2, operacao)
if __name__=='__main__':
    main()