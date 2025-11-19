def base_altura(base, alt):
    print('QUADRADO' if base == alt else
    (f' RETÂNGULO {base*2 +alt*2} - {base*alt}'))
def main():
    print('QUADRADO OU RETÂNGULO...')
    base = int(input('Digite Base: '))
    alt = int(input('Digite Altura: '))
    base_altura(base, alt)
if __name__=='__main__':
    main()