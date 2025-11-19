def tps_caracters(tipos):
    if tipos.isalpha():
        if tipos.lower() in 'aeiou':
            return 'Vogal'
        else:
            return 'Consoante'
    elif tipos.isdigit():
        return 'Numero'
    else:
        return 'Simbolo'
def main():
    caractere = input('Digite um caractere: ')
    print(f'Seu caractere é {tps_caracters(caractere)}')
if __name__=='__main__':
    main()