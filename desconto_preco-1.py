preco_produto = float(input('Preço do produto: ').strip())
desconto = 10 / 100
calculo = desconto * preco_produto
print(f'Preço do produto com DESCONTO DE 10%: {preco_produto - calculo:.2f}')