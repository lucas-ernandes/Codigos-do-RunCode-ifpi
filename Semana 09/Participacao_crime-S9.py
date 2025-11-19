def pergutas(resposta):
    return 1 if resposta == 's' else 0

def main():
    score = 0
    print('Senhor a gente vai lhe interrogar agora, responta apenas Sim(s) ou Não(n): ')
    
    perguntas = [
    "Telefonou para a vítima ? (s/n ",

    "Esteve no local do crime ? (s/n) ",

    "Mora perto da vítima ? (s/n) ",

    "Devia para a vítima ? (s/n) ",

    "Já trabalhou com a vítima ? (s/n) "
    ]
    respostas = [input(pergunta).lower().strip() for pergunta in perguntas]

    for resp in respostas:
        score += pergutas(resp)

    print('Suspeito' if score == 2 else 'Cúmplice' if score ==
          3 or score == 4 else 'Assassino' if score == 5 else 'Inocente')
if __name__ == '__main__':
    main()
