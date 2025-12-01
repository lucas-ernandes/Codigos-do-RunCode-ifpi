def esta_ordenad(lista_a):
    return all(a <= b for a, b in zip(lista_a, lista_a[1:]))

def ler_valor():
    entrada = input().strip()
    try:
        # tenta converter para número inteiro
        return int(entrada)
    except ValueError:
        try:
            # tenta converter para número real
            return float(entrada)
        except ValueError:
            # mantém como string
            return entrada

def main():
    lista_ah = []
    num = int(input().strip())
    
    for _ in range(num):
        lista_ah.append(ler_valor())
    
    if esta_ordenad(lista_ah):
        print('LISTA ORDENADA')
    else:
        print('LISTA NÃO ORDENADA')

if __name__ == '__main__':
    main()