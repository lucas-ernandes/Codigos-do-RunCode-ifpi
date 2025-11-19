def numeros_indefin(n1):
    #calcula a média
        media = sum(n1) / len(n1) #sum soma todos os numero da lista e divide pela quantidade (len)
        return media

#Saida
def main():
    #cria uma lista
    n1 = []
    #Cria um loop infinito q só para quando coloca um 'brake'
    print('Insira quantos números quiser! Quando estiver cansado digite 0: ')
    while True:
        numero = int(input().strip())
        if numero == 0:
            break
        if numero > 0:
            #colocado dentro da lista de numeros
            n1.append(numero)

    print(f'Sua média: {numeros_indefin(n1):.2f}')


if __name__ == '__main__':
    main()
