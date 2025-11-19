def fatorial(n):
    f = 1
    i = 1
    while i <= n:
        f *= i
        i += 1
    return f

# Programa principal
num = int(input())
resultado = fatorial(num)
print(resultado)