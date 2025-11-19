#Definido função que recebe (tempo)
def evento(tempo):
    #Calculo que converte o tempo
    cal_hora = tempo // 3600
    cal_min = (tempo % 3600) // 60
    seg = tempo % 60
    return f'{cal_hora:02d}:{cal_min:02d}:{seg:02d}'
#Processamento de dados
def main():
    hora = int(input('Quantos segundos durou o evento: ').strip())
    print(f'O evento durou {evento(hora)} no total.')
    #Saida de dados
if __name__ == '__main__':
    main()