def preencher_0(n):
    
    #a) preenche com 0 e imprimir
    lista = [0] * n
    print(f'a){lista}')
    return lista

def preencher_1(n):
    #b) preenche com numeros de 1 a n e imprimi
    lista = list(range(1, n+1))
    print(f'b){lista}')
    return lista

def preencher_2(n):
    lista = []
    #c) preenche com valores lidos pelos teclado
    for _ in range(n):
        valor = int(input().strip())
        lista.append(valor)
    print(f'c){lista}')
    return lista

def preencher_invertido(n):
    lista = []
    #d) preenche na ordem inversa usando insert no inicio
    for _ in range(n):
        valor = int(input().strip())
        lista.insert(0, valor) #insere no inicio
    print(f'd){lista}')
    return lista

def main():
    n = int(input('Digite um valor: ').strip())
    
    preencher_0(n)
    preencher_1(n)
    preencher_2(n)
    preencher_invertido(n)
    
if __name__=='__main__':
    main()