def centenas(n1):
    centenas = n1 // 100
    dezenas = (n1 % 100) //10
    unidade = n1%10
    
    numeros = []
    extenso =['zero', 'uma', 'duas', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
    if centenas >0:
      numeros.append('uma centena' if centenas == 1 else f'{extenso[centenas]} centenas')
    if dezenas > 0:
      numeros.append('uma dezena' if dezenas == 1 else f'{extenso[dezenas]} dezenas')
    if unidade > 0:
      numeros.append('uma unidade' if unidade == 1 else f'{extenso[unidade]} unidades')
      
    return(
    'nao tem nada aq pô!' if len(numeros) == 0 else
    f'{numeros[0]}.' if len(numeros) == 1 else
    f'{numeros[0]} e {numeros[1]}.' if len(numeros) == 2 else
    f'{numeros[0]}, {numeros[1]} e {numeros[2]}.')
def main():
    n1 = int(input('Insira um número de 1 a 1000: ').strip())
    print('APENAS DE 1 A 1000!')if n1 <0 or n1 >=1000 else print(centenas(n1))
if __name__=='__main__':
    main()