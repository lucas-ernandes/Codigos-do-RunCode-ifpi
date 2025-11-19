def soma_digitos(num):
    #Se variavel for q 100mil ou menor q 0, retorna -1
    if num >= 100000 or num < 0:
        return -1
    #Soma os digitos e transforma eles em string
    return sum(int(digito) for digito in str(num))
def main():
    numero = int(input('Digite um número de 0 até 100000: ').strip())
    print(soma_digitos(numero))
if __name__=='__main__':
    main()