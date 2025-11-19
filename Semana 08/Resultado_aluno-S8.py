def resultado(media_final):
    
    if media_final >= 9.0:
        return 'A'
    elif media_final >=7.5 and media_final <9.0:
        return 'B'
    elif media_final >=6 and media_final <7.5:
        return 'C'
    elif media_final >=4.0 and media_final <6.0:
        return 'D'
    elif media_final <4.0:
        return 'E'
def conceito(aprovacao):
    if aprovacao in ['A', 'B', 'C']:
        return 'Aprovado'
    else:
        return 'Reprovado'
def main():
    matricula = input('Digite sua matricula: ')
    nota_1 = float(input('Primeira nota: '))
    nota_2 = float(input('Segunda prova:'))
    nota_3 = float(input('Terceira prova: '))
    media_ex = float(input('Média dos exercicios: '))
    
    media_final = (nota_1 + nota_2*2 + nota_3*3 + media_ex) / 7
    conceito_final = resultado(media_final)
    situacao = conceito(conceito_final)
    print('Matricula:', matricula)
    print(f'Sua média final: {media_final:.2f}')
    print('Sua situação:', conceito_final)
    print('Resultado:', situacao)
if __name__=='__main__':
    main()