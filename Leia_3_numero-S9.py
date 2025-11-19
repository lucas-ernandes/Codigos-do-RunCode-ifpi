def ler_numero(n1, n2, n3):
    print('Todos os valores são diferentes'if n1 != n2 and n1 != n3 and n2 != n3 else 'Todos os valores são iguais'if n1 == n2 and n1 ==n3 and n2==n3  else 'Existem dois valores iguais e um diferente')
def main():
    n1 = int(input('Insira o primeiro número: '))
    n2 = int(input('Insira o segundo número: '))
    n3 = int(input('Insira o terceiro número: '))
    ler_numero(n1, n2, n3)
if __name__=='__main__':
    main()