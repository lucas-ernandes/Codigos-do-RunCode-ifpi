def popula_pais(p1, p2):
    taxaA = 0.02
    taxaB = 0.03
    
    anos = 0
    
    if p1 <p2:
        p1, p2 = p2, p1
    
    while p2 <= p1:
        p1 += p1 * taxaA
        p2 += p2 * taxaB
        anos += 1
    return anos
def main():
    paisA = int(input().strip())
    paisB = int(input().strip())
    
    print(popula_pais(paisA, paisB))
if __name__=='__main__':
    main()