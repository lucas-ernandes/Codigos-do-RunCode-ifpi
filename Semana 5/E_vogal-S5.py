# Processamento de Dados
def so_volgal(letra):
    # String sera verdadeira se for vogal
    return letra.lower() in 'aeiou'

# Programa principal

def main():
#Entrada
    l = input('Digite uma letra: ')
    print(f'Sua letra é: {so_volgal(l)}')

#Saida
if __name__ == '__main__':
    main()
