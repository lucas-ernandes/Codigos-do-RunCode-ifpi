def qtd_pares(numero):
# Converte o número para string para poder percorrer dígito por dígito
    digitos = str(numero)
 #Inicializa o contador de dígitos pares
    par = 0
# -Para- cada caractere (dígito) na string
    for d in digitos:
        if int(d) % 2 == 0: #Verificar se o digito é par
            par += 1 #Se for par, incrementa o contador
    return par #Retorna a qtd total de digitos pares
#Processo de Ddos
def main():
    pares = int(input('Digite um numero de 100 até 999: '))
    print(f'Seu número tem: {qtd_pares(pares)} pares')
if __name__=='__main__':
    main()