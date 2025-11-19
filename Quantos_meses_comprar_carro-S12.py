def meses_para_comprar(carro):
    poupanca = 10000
    rendimento = 0.007   # 0,7% ao mês
    aumento_carro = 0.004  # 0,4% ao mês
    meses = 0

    while poupanca < carro:
        poupanca *= (1 + rendimento)
        carro *= (1 + aumento_carro)
        meses += 1

    return meses

def main():
    preco = float(input().strip())
    meses = meses_para_comprar(preco)
    print(meses)

if __name__ == "__main__":
    main()