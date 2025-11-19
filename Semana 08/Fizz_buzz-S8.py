def fizzbuzz(divisor):
    
    if divisor % 3 == 0 and divisor % 5 ==0:
        print('Seu numero é: FIZZBUZZ')
    elif divisor % 3 == 0:
        print('Seu número é: FIZZ')
    elif divisor % 5 ==0:
        print('Seu número é: BUZZ')
    else:
        print(divisor)
def main():
    numero = int(input('Digite um número positivo: '))
    fizzbuzz(numero)
if __name__=='__main__':
    main()