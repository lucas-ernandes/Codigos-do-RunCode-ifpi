def numeros_invertido(n1):
    #Converte o numero para string e inverte ele '::-1'
    inverter = int(str(n1)[::-1])

    return inverter

#Saida
def main():
    #Cria um loop infinito q só para quando coloca um 'brake'
    print('Insira um número que o programa irá invertelo!')
    while True:
        numero = int(input().strip())
        
        sla = numeros_invertido(numero)
        print('Invertido:',sla)
        break

if __name__ == '__main__':
    main()
