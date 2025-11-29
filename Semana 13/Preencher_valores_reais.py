def valores_reais(n):
    #A)
    if n == 0:
        print([])
        return []

    lista = []
    for _ in range(n):
        valor = float(input().strip())
        lista.append(valor)
        
    lista = lista[::-1]
    print(lista)
    return lista

def media(n):
    #B)
    if n == 0:
        print([])
        print('SEM NOTAS')
        return []

    notas = []
    for _ in range(n):
        nota = float(input().strip())
        notas.append(nota)

    media_nota = sum(notas) / n
    print(notas)
    print(round(media_nota,1))
    
    return notas


def letras(n):
    #C)
    if n == 0:
        print(0)
        print([])
        return []
    
    lista = []
    for _ in range(n):
        letra = input().strip()
        lista.append(letra)
        
    vogais = 'aeiouAEIOU'
    #calculo da qtd de vogais lidas
    qtd = sum( 1 for l in lista if l in vogais)
    consoantes = [l for l in lista if l not in vogais]

    print(qtd)
    print(consoantes)

    return lista


def main():
    n = int(input().strip())
    
    valores_reais(n)
    media(n)
    letras(n)

if __name__ == '__main__':
    main()