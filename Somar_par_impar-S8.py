def somar_imp_par(numero):
    if numero % 2 !=0:
        numero +=8
    elif numero % 2 ==0:
        numero +=5
    print(numero)
def main():
    num = int(input('Digite um número: '))
    somar_imp_par(num)
if __name__=='__main__':
    main()