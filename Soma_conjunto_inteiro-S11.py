def numeros_indefin(n1):
    #calcula a soma
        soma = sum(n1) #sum soma todos os numero da lista
        return soma

#Saida
def main():
    #cria uma lista
    n1 = []
    #Cria um loop infinito q só para quando coloca um 'brake'
    while True:
        numero = int(input('Digite quantos numeros quiser, e digite 0 pra saber a soma total: ').strip())
        if numero == 0:
            break
        if numero > 0:
            #colocado dentro da lista de numeros
            n1.append(numero)

    print(f'{numeros_indefin(n1)}')

if __name__ == '__main__':
    main()
