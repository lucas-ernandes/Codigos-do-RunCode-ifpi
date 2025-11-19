def menu(n1):
    seleciona = len(n1)
    return seleciona
def main():
    opcoes = []
    cardapio = {
        'H': 5.50,
        'C': 6.80,
        'M': 4.50,
        'A': 7.00,
        'Q': 4.00
    }
    total = 0
    
    while True:
        sla = input().upper().strip()
        opcoes.append(sla)
        if sla == 'X':
            break
        if sla in cardapio:
            total += cardapio[sla]
    for opcao in opcoes:
        if opcao == 'H':
            print('''CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5,50
C       Cheeseburger    6,80
M       Misto Quente    4,50
A       Americano       7,00
Q       Queijo Prato    4,00
X       PARA TOTAL DA CONTA''')
        elif opcao == 'C':
            print('''CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5,50
C       Cheeseburger    6,80
M       Misto Quente    4,50
A       Americano       7,00
Q       Queijo Prato    4,00
X       PARA TOTAL DA CONTA''')
        else:
            print('''CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5,50
C       Cheeseburger    6,80
M       Misto Quente    4,50
A       Americano       7,00
Q       Queijo Prato    4,00
X       PARA TOTAL DA CONTA''')
    print(f'{total:.2f}')
if __name__=='__main__':
    main()