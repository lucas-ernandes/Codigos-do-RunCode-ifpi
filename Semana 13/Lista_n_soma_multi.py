def lista_numero(n):
    print(n)
    print(sum(n))

#multiplicação
    numero = 1  #cada numero da lista vai ser multiplicado por ele
    for i in n:
        numero *= i
    print(f'Sua lista multiplicada:', numero)
    
def main():
    lista = []
    for i in range(10):
        numero = int(input(f'Digite o número {i+1}: ').strip())
        lista.append(numero)
        
    lista_numero(lista)
    
if __name__=='__main__':
    main()