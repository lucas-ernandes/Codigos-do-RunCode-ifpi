def max_min(n1, n2, n3, n4, n5):
    #achar o maior
    if n1 >= n2 and n1>=n3 and n1 >=n4 and n1 >=n5:
        max = n1
    elif n2 >= n1 and n2>=n3 and n2 >=n4 and n2 >=n5:
        max = n2
    elif n3 >= n1 and n3>=n2 and n3 >=n4 and n3 >=n5:
        max = n3
    elif n4 >= n1 and n4>=n2 and n4 >=n3 and n4 >=n5:
        max = n4
    else:
        max = n5
    #achar o menor
    if n1 <= n2 and n1<=n3 and n1 <=n4 and n1 <=n5:
        min = n1
    elif n2 <= n1 and n2<=n3 and n2 <=n4 and n2 <=n5:
        min = n2
    elif n3 <= n1 and n3<=n2 and n3 <=n4 and n3 <=n5:
        min = n3
    elif n4 <= n1 and n4<=n2 and n4 <=n3 and n4 <=n5:
        min = n4
    else:
        min = n5
    #imprimir    
    print(f'Maior número: {max}')
    print(f'Menor número: {min}')
    
#Função principal
def main():
    num_1 = int(input('Digite um número: '))
    num_2 = int(input('Digite um número: '))
    num_3 = int(input('Digite um número: '))
    num_4 = int(input('Digite um número: '))
    num_5 = int(input('Digite um número: '))
    max_min(num_1, num_2, num_3, num_4, num_5)
if __name__=='__main__':
    main()