def valor_dobro(n1, n2):
    #Contador de anos, começa com 0
    anos = 0
    valor = n1
    #converter para decimal
    taxa = n2 /100
    
    while valor <2 * n1:
        #aplicando a taxa
        valor += valor * taxa
        #conta mais 1
        anos += 1
    return anos
#Saida
def main():
    valor_ini = int(input('Digite o valor Inicial: ').strip())
    taxa = float(input('Qual a taxa de juros por ano: ').strip())
    
    print(valor_dobro(valor_ini, taxa), 'anos')
if __name__=='__main__':
    main()