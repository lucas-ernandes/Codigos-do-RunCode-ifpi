def num_letra(letra):
    return len(letra)
def main():
    letra = input('Insira uma frase: ').strip()
    print(f'Sua frase tem {num_letra(letra)} letras!')
if __name__ == '__main__':
    main()
