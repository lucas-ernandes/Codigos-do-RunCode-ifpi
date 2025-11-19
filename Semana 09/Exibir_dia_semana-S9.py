def semana(n1):
    print(
        'domingo' if n1 ==1 else
        'segunda-feira' if n1==2 else
        'terça-feira' if n1==3 else
        'quarta-feira' if n1==4 else
        'quinta-feira' if n1==5 else
        'sexta-feira' if n1==6 else
        'sábado' if n1==7 else 'valor inválido'
    )
def main():
    dia_semena = int(input('Digite um dia da semema aí: '))
    semana(dia_semena)
if __name__ == '__main__':
    main()