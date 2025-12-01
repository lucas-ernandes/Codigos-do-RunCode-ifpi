def multiplica_constante(n1):
    lista_sla  = []
    constante = int(input().strip())

    for x in n1:
        lista_sla.append(constante * x)
    return lista_sla

def main():
    num_list = []
    while True:
        n = int(input().strip())
        if n == 0:
            break
        num_list.append(n)
        
    sla = multiplica_constante(num_list)
    print(sla)
if __name__=='__main__':
    main()