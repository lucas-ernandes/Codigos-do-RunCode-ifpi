def ordem_cres(n1, n2, n3):
    #Condições de ordem menor para o maior
    if n1 <= n2 <= n3:
        return n1, n2, n3
    elif n1 <= n3 <= n2:
        return n1, n3, n2
    elif n3 <= n1 <= n2:
        return n3, n1, n2
    elif n3 <= n2 <= n1:
        return n3, n2, n1
    elif n2<= n3 <= n1:
        return n2, n3, n1
    else:
        return n2, n1, n3
#Processo de Dados
def main():
    num_1 = int(input('Digite o primeiro número: '))
    num_2 = int(input('Digete o segundo número: '))
    num_3 = int(input('Digite o terceiro número: '))
    ordem = ordem_cres(num_1, num_2, num_3)
    for i in ordem:
        print(i)
if __name__=='__main__':
    main()