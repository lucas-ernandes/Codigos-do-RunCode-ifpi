def main():
    salariu = float(input('Salário: ').strip())
    divida = float(input('Divida: ').strip())

    mes = 10
    ano = 2016
    
    while divida <= salariu:
        divida *= 1.15
        
        if mes == 3:
            salariu*= 1.05
        mes += 1
        
        if mes >12:
            mes =1
            ano += 1
    print(f'Resultado: {mes}/{ano}')
if __name__=='__main__':
    main()