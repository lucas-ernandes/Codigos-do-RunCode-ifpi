#Desenvolva um programa que peça ao usuário o nível de volume atual e o nível de volume desejado de seu aparelho de som. Calcule e mostre a diferença de volume necessária.

vol = int(input('Nivel de volume atual: ').strip())
volume = int(input('Nivel de volume desejado: ').strip())
diferenca = vol - volume
print(f'A diferença de volume é: {diferenca}, Aumente ou Diminua para alteração!')
