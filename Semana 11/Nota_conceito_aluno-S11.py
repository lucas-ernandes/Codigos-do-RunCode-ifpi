def menu(nota):
    # condições da nota, de 0 até 10
    if nota >10 or nota <0:
        print('Nota inválida.')
        
    elif nota >= 8.5:
        print('A')
    elif nota >= 7:
        print('B')
    elif nota >= 5:
        print('C')
    elif nota >= 4:
        print('D')
    else:
        print('E')
        
#Entrada principal
def main():
    print(''' Digite sua nota para saber seu resultado:
=============================================''')
    #repetição se for menor q 0 ou maior 10
    while True:
        sla = float(input().strip())
        
        if 0 <= sla <=10:
           break
        else:
            print('Nota inválida.')
#saida
    print('Sua SITUAÇÃO é:') , menu(sla)
if __name__=='__main__':
    main()