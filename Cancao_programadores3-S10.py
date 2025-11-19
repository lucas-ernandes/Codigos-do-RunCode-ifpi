def cancao():
    #Uso de repetição, iniciando de 99 e pulando de 7 em 7 até 250
    for i in range(99, 251, 7):
        print(f'{i} bugs no software, pegue sete deles e conserte... \nTecle "Ctrl+F5"')
    #finaliza com uma frase após o ultimo número
    print('Vamos fazer mais um café!')
#função principal
def main():
    cancao()
if __name__=='__main__':
    main()