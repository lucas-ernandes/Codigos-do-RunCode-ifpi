def sorte(n1):
    soma = 0
    i = 0
    while i < len(n1):
        soma += int(n1[i])
        i += 1
    return soma
def main():
    data = input().strip()
    print(sorte(data))
if __name__=='__main__':
    main()