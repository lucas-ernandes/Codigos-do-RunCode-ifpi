def multiplica_doido(n1):
    lista_sla  = sorted(n1)
    
    #percorre a lista usando os índices
    for x in range(len(lista_sla)):
        if x % 2 ==0 :
            lista_sla[x] *= 3
        else:
            lista_sla[x] *= 5

    return lista_sla

#Principal
def main():
    num_list = []
    
    for x in range(100):
        sla = int(input().strip())
        num_list.append(sla)
        
    print(multiplica_doido(num_list))
if __name__=='__main__':
    main()