def main():
     n1 = int(input().strip())

     h = 0.0
     i = 1
     
     #enquanto o i for menor q n1, soma 1 / i
     while i <= n1:
         h += 1/i
         i += 1
     print(f'{h:.4f}')
if __name__=='__main__':
    main()