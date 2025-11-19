def media_maior(n1, n2, n3, n4, n5):
    media = (n1 + n2 + n3 + n4 + n5) / 5
    print(f'Sua média: {media:.2f}')
    print('Números maiores que a média!')
    if n1 > media:
        print(f'{n1:.2f}')
    if n2 > media:
        print(f'{n2:.2f}')
    if n3> media:
        print(f'{n3:.2f}')
    if n4> media:
        print(f'{n4:.2f}')
    if n5> media:
        print(f'{n5:.2f}')
#Função principal
def main():
    num_1 = int(input())
    num_2 = int(input())
    num_3 = int(input())
    num_4 = int(input())
    num_5 = int(input())
    media_maior(num_1, num_2, num_3, num_4, num_5)
if __name__=='__main__':
    main()