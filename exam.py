import struct


def create_file():
    n = int(input('Введите размерность матрицы: '))
    
    a = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            a[i][j] = int(input(f'Введите {i+1}-й {j+1}-й элемент: '))
    
            


def main():
    create_file()


if __name__ == '__main__':
    main()