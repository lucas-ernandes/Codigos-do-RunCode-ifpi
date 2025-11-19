def diferenc_valor(n1, n2, n3):
    diferenca_1 = abs(n1 - n2)
    diferenca_2 = abs(n1 - n3)
    
    print(f' Segundo valor está mais proximo do 1º: {diferenca_1}' if diferenca_1 < diferenca_2 else
    f'3º está mais proximo do 1º: {diferenca_2}' if diferenca_2 < diferenca_1 else f'O 2º e o 3º valor estão igualmente proximo do 1º: {diferenca_1}')

def main():
    print('Mostrando a diferença dos valores:')
    n1 = int(input('1º Valor: '))
    n2 = int(input('2º Valor: '))
    n3 = int(input('3º Valor: '))
    diferenc_valor(n1, n2, n3)
if __name__=='__main__':
    main()