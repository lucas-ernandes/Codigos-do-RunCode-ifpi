import math

def tempo_tarta(distancia):
    # calcula em quantos minutos a lebre alcança a tartaruga
    vel_tartaruga = 1
    vel_lebre = 10
    diferenca = vel_lebre - vel_tartaruga
    tempo = math.ceil(distancia / diferenca)
    return tempo

def main():
    metros_afrente = float(input().strip())
    print(tempo_tarta(metros_afrente))

if __name__ == '__main__':
    main()