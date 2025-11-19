def fibonacci(n1):
    #defindo os valores do termo
    f1 = 0
    f2 = 1

    #imprimir antes do laço e tudo na mesma linha
    print(f'{f1}, {f2}', end=', ')
    
    #Calcular os proximos termos
    for i in range(2, n1):
        f3 = f1 + f2
        f1, f2 = f2, f3
        
        if i == n1 - 1:
            print(f'{f3}', end='')
        else:
            print(f3, end=', ')
            
    #Principal
def main():
    n = int(input().strip())
    fibonacci(n)
    
if __name__=='__main__':
    main()