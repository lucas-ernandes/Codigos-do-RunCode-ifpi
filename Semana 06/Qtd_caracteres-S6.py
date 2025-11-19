#definindo uma função que recebe (nome)
def qtd_letras (nome):
    #função que será chamada na função principal
    return len(nome)

#processo de dados
def main():
    qtd = input().strip()
    print(qtd_letras(qtd))
    #Saída
if __name__ == '__main__':
    main()