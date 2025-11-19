def preco_acrescimo(valor, desconto):
    return valor + (valor * desconto / 100)


def preco_descontado(valor, desconto):
    return valor - (valor * desconto / 100)

def main():
    valor_preco = float(input('Valor: '))
    percentual = float(input('Valor do percentual: '))
    
    print(f'O valor do seu preço com acrescimo fica: {preco_acrescimo(valor_preco, percentual):.2f}')
    print(f'O valor com desconto fica: {preco_descontado(valor_preco, percentual):.2f}')
    
if __name__ == '__main__':
    main()
