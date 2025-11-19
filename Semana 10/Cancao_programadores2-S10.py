def cancao():
    #Uso de repetição, vai de 99 ate 250 com a frase abaixo.
    for i in range(99, 251):
        print(f'{i} bugs no software, pegue um deles e conserte... \nTecle "Ctrl+F5"')
    #finaliza com uma frase após o ultimo número
    print('Vamos fazer mais um café!')
#função principal
def main():
    cancao()
if __name__=='__main__':
    main()