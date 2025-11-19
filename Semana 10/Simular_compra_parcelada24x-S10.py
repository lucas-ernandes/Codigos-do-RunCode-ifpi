def main():
    #colocando variavel entrada
    valor = int(input().strip())
    #repeticao da parcela de 1x até 24x, e dividino pela variavel
    for i in range(1, 25):
        parcela = valor/i
        print(f'{i}x de R$ {parcela:.2f}')
if __name__=='__main__':
    main()