def soma_cumulativa(n1):
    lista_sla  = []
    total = 0
    #soma cada valor ao 'total' e guarda o resultado na lista acumulada
    for x in n1:
        total += x
        lista_sla.append(total)
       
    return lista_sla
#entrada principal
def main():
    num_list = []
    while True:
        n = int(input().strip())
        if n == 0:
            break
        num_list.append(n)
        
    print(soma_cumulativa(num_list))
if __name__=='__main__':
    main()