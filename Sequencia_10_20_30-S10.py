def num_media():
    numeros = []
    for i in range(10, 1001, 10):
        ponto = '.' if i == 1000 else ', '
        print(i, end=ponto)
def main():
    num_media()
if __name__=='__main__':
    main()