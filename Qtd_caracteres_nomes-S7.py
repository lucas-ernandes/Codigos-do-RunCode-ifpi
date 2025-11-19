def casados(souteiro, estado_civil):
    if estado_civil == 1:
        nome = input('Nome do cônjuge: ').strip()
        return len(nome) + len(souteiro)
    elif estado_civil == 2:
        return len(souteiro)
    else:
        return 0
def main():
    nome = input('Seu nome: ').strip()
    estado_civi = int(input('Digite 1(Casado) ou 2(Solteiro): ').strip())
    print(f' A quantidade de letra da relação é : {casados(nome, estado_civi)}')
if __name__=='__main__':
        main()
    