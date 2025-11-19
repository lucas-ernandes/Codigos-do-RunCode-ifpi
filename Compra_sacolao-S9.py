def sacolao(kg_mora, kg_maca):
    preco_moran = kg_mora * (2.50 if kg_mora <=5 else 2.20)
    preco_maca = kg_maca * (1.80 if kg_maca<= 5 else 1.50)

    peso_total = kg_mora + kg_maca
    valor_total = preco_moran + preco_maca
    
    valor_total = valor_total * 0.90 if peso_total >8 or valor_total >25 else valor_total
    return f'O valor a ser pago é : {valor_total:.2f} Reais'
def main():
    print('Calculo da compra do sacolão!')
    morango = float(input('Você comprou quantos Kg de morango? '))
    maca = float(input('Quantos Kg de maça: '))
    print(sacolao(morango, maca))
if __name__=='__main__':
    main()