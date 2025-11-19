def muier_homi(*sexo):
    return sexo

def main():
    nome = input('Seu nome: ')
    genero = int(input('1-homem ou 2-mulher: '))

    if genero == 1:
        print(f'Ilmo Sr. {nome}')
    else:
        print(f'Ilma Sra. {nome}.')

if __name__ == '__main__':
    main()
