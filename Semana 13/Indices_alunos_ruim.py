def notas_alun(n1):
    notas = []
    for x in range(len(n1)):
        if n1[x] >= 6:
            notas.append(x)
    return notas
#ENtrada principal
def main():
    lista_aluno = []
    for i in range(50):
        alunos = float(input().strip())
        lista_aluno.append(alunos)
        
    print(notas_alun(lista_aluno))
if __name__=='__main__':
    main()