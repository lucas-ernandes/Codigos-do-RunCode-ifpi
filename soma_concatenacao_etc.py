#variaveis recebem strings
x = input().strip()
y = input().strip()
#variaveis recebem numeros reais, e 'string1' recebe um numero com uma casa decimal
string1 = f"{float(x):.1f}"
num_1 = float(x)
num_2 = float(y)
#calculos
cal_1 = num_1 + num_2
cal_2 = string1 + y
cal_3 = num_1 * num_2
cal_4 = string1 * int(num_2)
cal_5 = num_1 / num_2
cal_6 = num_1 // num_2
cal_7 = num_1 ** num_2
cal_8 = num_1 % num_2
#mostranto na tela os resultados
print(cal_1)
print(cal_2)
print(cal_3)
print(cal_4)
print(cal_5)
print(cal_6)
print(cal_7)
print(cal_8)