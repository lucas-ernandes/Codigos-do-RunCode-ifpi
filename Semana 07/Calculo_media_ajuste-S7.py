#Defindo função
def media(nota1, nota2, nota3):
    medii_a = (nota1 + nota2 + nota3) /3
#Aplicando ponto extra se nota3 for maior q 8
    if nota3 > 8:
        medii_a += 1
# Garantino q a média final não passe de 10
    if medii_a > 10:
        medii_a = 10
    return medii_a
#Processamento de dados
def main():
    nota1 = int(input('Primeira nota: '))
    nota2 = int(input('Segunda nota: '))
    nota3 = int(input('Terceira nota: '))
    resultado = media(nota1, nota2, nota3)
    print(f'Sua media é: {resultado:.2f}')
if __name__=='__main__':
        main()