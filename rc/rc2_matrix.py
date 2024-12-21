def rotate_matrix_90_clockwise(input_filename, output_filename):
    """
    Считывает квадратную матрицу из файла input_filename,
    поворачивает её на 90 градусов по часовой стрелке и записывает в файл output_filename.
    :param input_filename: Имя файла с исходной матрицей.
    :param output_filename: Имя файла для записи результата.
    """
    # Считываем матрицу построчно
    with open(input_filename, 'r') as infile:
        # Считываем строки и разбиваем их на элементы
        lines = infile.readlines()

    n = len(lines)  # Размерность матрицы (предполагаем, что матрица квадратная)

    # Открываем файл для записи
    with open(output_filename, 'w') as outfile:
        for j in range(n):  # Для каждого столбца исходной матрицы
            first = True
            for i in range(n-1, -1, -1):  # Проходим по строкам исходной матрицы (снизу вверх)
                number = lines[i].split()[j]  # Берем элемент из i-й строки и j-го столбца
                if first:
                    outfile.write(number)
                    first = False
                else:
                    outfile.write(' ' + number)
            outfile.write('\n')  # Переход на новую строку после записи столбца

# Пример использования
if __name__ == "__main__":
    input_filename = 'in1.txt'
    output_filename = 'out1.txt'
    
    # Поворачиваем матрицу на 90 градусов по часовой стрелке и записываем результат в файл out1.txt
    rotate_matrix_90_clockwise(input_filename, output_filename)
