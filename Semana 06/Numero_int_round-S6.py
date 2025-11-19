def  financia(numero):
    return round(numero)

def main():
    num = float(input('Insira um valor em reais: '))
    print(f'Seu dinheiro fica arredondado para: {financia(num)} Reais')
if __name__=='__main__':
    main()
