def anos_espacial(ano):
    ano_terrestre = ano // 2
    return round(ano_terrestre)
def main():
    idade = int(input('Digite sua idade: '))
    print(f' Sua idade em anos espaciais é: {anos_espacial(idade)}')
if __name__=='__main__':
    main()