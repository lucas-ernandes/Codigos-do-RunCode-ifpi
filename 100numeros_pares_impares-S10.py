def num_inteiros():
    numeros = []
    for i in range(100):
        num = int(input())
        numeros.append(num)

    pares = sum(1 for n in numeros if n %2 ==0)
    impares =len(numeros) - pares
    print(pares)
    print(impares)
def main():
    num_inteiros()
if __name__=='__main__':
    main()