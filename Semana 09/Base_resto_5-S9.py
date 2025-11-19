def resto_5(n1):
    divi = n1 % 5
    if divi == 0:
        print(9 * n1 + 7)
    elif divi == 1:
        print('par' if n1 % 2==0 else 'ímpar')
    else:
       print(
          5 * (n1 ** 2) - 3 * n1 + 42 if divi == 2 else
          n1 // 10 if divi == 3 else
          n1 ** 2 if divi == 4 else
          "Condição não atendida")
    
def main():
    print('Valor com base no resto da divisão(5):')
    resto = int(input('Digite um número: '))
    resto_5(resto)
if __name__=='__main__':
    main()
  