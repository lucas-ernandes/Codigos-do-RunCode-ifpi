def cancao():
    #Uso de repetição, iniciando de 99 e tirando 11 a 11 até a 0
    for i in range(99, 0, -11):
        print(f'{i} bugs no software, pegue onze deles e conserte... \nTecle "Ctrl+F5"')
    #finaliza com uma frase após o ultimo número
    print('Sem erros no software! Está estabilizado!')
#função principal/saida
def main():
    cancao()
if __name__=='__main__':
    main()