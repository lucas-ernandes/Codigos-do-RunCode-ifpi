def lista_intercalar(a, b):
    lista_c = []
    
    for x, y in zip(a, b):
        lista_c.append(x)
        lista_c.append(y)
    return lista_c


def main():
    lista_a = []
    lista_b = []
    
    for i in range(1, 26):
        lista_a.append(int(input().strip()))
      
    for i in range(1, 26):  
        lista_b.append(int(input().strip()))
      
    print(lista_a)
    print(lista_b)
    
    print(lista_intercalar(lista_a, lista_b))
if __name__ == '__main__':
    main()