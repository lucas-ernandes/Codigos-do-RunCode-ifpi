def main():
    pop_inicial = int(input().strip())

    pop_atual = pop_inicial
    ano = 1600

    while pop_atual >= 0.1 * pop_inicial:
        mortes = max(1 ,int(pop_atual * 0.06 + 0.5))
        nascimentos = max(1, int(pop_atual * 0.01 + 0.5))
        pop_atual = pop_atual - mortes + nascimentos
        print(f"{ano}, {nascimentos}, {mortes}, {pop_atual}")
        ano += 1
    
if __name__=='__main__':
    main()