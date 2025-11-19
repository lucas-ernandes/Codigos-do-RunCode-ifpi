def menu(n1):
    seleciona = len(n1)
    return seleciona
def main():
    opcoes = []
    while True:
        sla = int(input())
        opcoes.append(sla)
        if sla == 0:
            break
    for opcao in opcoes:
        if opcao == 1:
            print('''OPÇÕES:
1 - SAUDAÇÃO 
2 - BRONCA 
3 - FELICITAÇÃO 
0 - FIM
1 - Olá. Como vai?''')
        elif opcao == 2:
            print('''OPÇÕES:
1 - SAUDAÇÃO 
2 - BRONCA 
3 - FELICITAÇÃO 
0 - FIM
2 - Vamos estudar mais.''')
        elif opcao == 3:
            print('''OPÇÕES: 
1 - SAUDAÇÃO 
2 - BRONCA 
3 - FELICITAÇÃO 
0 - FIM
3 - Meus Parabéns!''')
        elif opcao == 0:
             print('''OPÇÕES: 
1 - SAUDAÇÃO 
2 - BRONCA 
3 - FELICITAÇÃO 
0 - FIM
0 - Fim de serviço.''')
        else:
            print('''OPÇÕES: 
1 - SAUDAÇÃO 
2 - BRONCA 
3 - FELICITAÇÃO 
0 - FIM
Opção inválida.''')
if __name__=='__main__':
    main()