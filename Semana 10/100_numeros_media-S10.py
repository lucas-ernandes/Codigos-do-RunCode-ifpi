def num_media():
    numeros = []
    for i in range(100):
        num = int(input('Digite um conjuto de 100 números: '))
        numeros.append(num)
    media = sum(numeros)/100
    print(f'{media:.2f}')
def main():
    num_media()
if __name__=='__main__':
    main()