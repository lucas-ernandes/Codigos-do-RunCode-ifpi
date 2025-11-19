def primo_o(n1):
    if n1 <= 1:
        return False
    
    divisor = 2
    while divisor <n1:
        if n1 % divisor ==0:
            return False
        divisor +=1
    return True
def main():
    x = int(input())
    y = int(input())

    if x > y:
        x, y = y, x
        #começa no inicio do intervalo
    num = x

    while num <= y:
        if primo_o(num):
            print(num)
        num +=1  
if __name__=='__main__':
    main()