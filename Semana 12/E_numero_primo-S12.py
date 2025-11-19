def e_primo(n1):
    if n1 <= 1:
        return False
    
    i = 2
    while i * i <= n1:
        if n1 % i ==0:
            return False
        i += 1
        
    return True
def main():
    numero = int(input().strip())

    print(e_primo(numero))
if __name__=='__main__':
    main()