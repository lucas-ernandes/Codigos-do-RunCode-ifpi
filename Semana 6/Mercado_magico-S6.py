def magia_negra(maca, banana):
    calculo = maca *3
    calculo_2 = banana *2
    soma = calculo + calculo_2
    return soma

def main():
    preco_maca = float(input('Digite o preço da maça: '))
    preco_banana = float(input('Digite o preço da banana: '))
    print(f'A soma toltal da compra das frutas é: ${magia_negra(preco_maca, preco_banana):.2f} Reais')
if __name__=='__main__':
    main()
    