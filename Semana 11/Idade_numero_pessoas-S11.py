def numeros_indefin(n1):
    #calcula a média
        qtd = len(n1) #sum soma todos os numero da lista e divide pela quantidade (len)
        media = sum(n1) / len(n1)
        maximo = max(n1)
        menor = min(n1)
        
        print('Quantidade:', qtd)
        print(f'Média das idade: {media:.2f}')
        print('Menor idade:', menor)
        print('Maior idade', maximo)
    
#Saida
def main():
    #cria uma lista
    n1 = []
    #Cria um loop infinito q só para quando coloca um 'brake'
    print('Digite as idades das pessoas que participaram da corrida: ')
    while True:
        numero = int(input().strip())
        if numero == 0:
            break
        if numero > 0:
            #colocado dentro da lista de numeros
            n1.append(numero)

    numeros_indefin(n1)


if __name__ == '__main__':
    main()
