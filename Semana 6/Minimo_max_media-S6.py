def min_max_md(numero):
    return numero
def main():
    num_1 = int(input('Digite 5 numeros: '))
    num_2 = int(input())
    num_3 = int(input())
    num_4 = int(input())
    num_5 = int(input())
    maximo = max(num_1, num_2, num_3, num_4, num_5)
    menor = min(num_1, num_2, num_3, num_4, num_5)
    media = (num_1+ num_2+ num_3+ num_4+ num_5) / 5
    print(f'O Maior numero é: {maximo}.')
    print(f'O Menor número é: {menor}')
    print(f'A média dos números digitados é: {media}.')
if __name__=='__main__':
    main()