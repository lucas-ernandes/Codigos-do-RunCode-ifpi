fatias = int(input('Quantas fatias de pizza tem?: ').strip())
amigos = int(input('Quantos amigos: ').strip())
sobra = fatias % amigos
print(f'Cada um recebe {fatias // amigos}')
print(f'Sobra {sobra} fatias.')
