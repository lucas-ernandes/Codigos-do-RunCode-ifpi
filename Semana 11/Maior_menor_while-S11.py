def numeros_indefin(n1):
    #define o maior e o menor
        maior = max(n1)
        menor = min(n1)

        return maior, menor

#Saida
def main():
    #cria uma lista
    n1 = []
    #Cria um loop infinito q só para quando coloca um 'brake'
    print('Insira quantos números quiser! Quando estiver cansado digite 0! ')
    while True:
        numero = int(input().strip())
        if numero == 0:
            break
        if numero > 0:
            #colocado dentro da lista de numeros
            n1.append(numero)
    maior, menor = numeros_indefin(n1)
    print('Maior:' , maior)
    print('Menor:' , menor)

if __name__ == '__main__':
    main()
