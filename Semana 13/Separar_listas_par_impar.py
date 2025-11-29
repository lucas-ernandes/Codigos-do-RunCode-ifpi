def num_par(n):
    par = []
    impa = []
    for num in n:
        if num % 2 == 0:
            par.append(num)
        else:
            impa.append(num)
    return par, impa


def main():
    lista = []
    for i in range(20):
        num = int(input().strip())
        lista.append(num)
    print(lista)
    pares, impares = num_par(lista)
    print(pares)
    print(impares)

if __name__ == '__main__':
    main()
