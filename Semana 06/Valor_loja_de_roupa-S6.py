def compra_deconto(preco):
    return preco - (preco*9 /100)
def preco_etiqueta(preco):
    return preco / 5
def compra_acrescimo(preco):
    percentual = preco + (preco*17 / 100)
    return percentual / 10

def main():
    preco = int(input('Valor de suas compras: '))
    print(f'Valor com 9% de desconto: {compra_deconto(preco):.2f}')
    print(f'Valor dividido em 5 prestação: {preco_etiqueta(preco):.2f}')
    print(f'Valor dividido em 10 prestação com juros de 17%: {compra_acrescimo(preco):.2f}')
if __name__=='__main__':
    main()