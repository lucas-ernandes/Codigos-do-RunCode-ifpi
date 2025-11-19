def idade_exata(D_atual, M_atual, A_atual, D_nasc, M_nasc, A_nasc):
    idade = A_atual - A_nasc
    if M_atual < M_nasc:
        idade -= 1
    else:
        if M_atual == M_nasc:
            if D_atual < D_nasc:
                idade -= 1
    return idade
def main():
    a_data = int(input('Data atual: '))
    a_mes = int(input('Mês atual: '))
    a_ano = int(input('Ano atual: '))
    print('Sua data de aniversario')
    n_data = int(input('Data de nasci: '))
    n_mes = int(input('Mês de nasci: '))
    n_ano = int(input('Ano de nasci: '))
    idade = idade_exata(a_data, a_mes, a_ano, n_data, n_mes, n_ano)
    print(f'Sua idade atual é: {idade} anos.')
if __name__=='__main__':
    main()