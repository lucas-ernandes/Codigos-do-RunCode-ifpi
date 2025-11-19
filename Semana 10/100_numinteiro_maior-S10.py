def maioR_numero():
    numeros = []
    for i in range(100):
        num = int(input())
        numeros.append(num)
    maior = max(numeros)
    print(f'{maior}')
def main():
    maioR_numero()
if __name__=='__main__':
    main()