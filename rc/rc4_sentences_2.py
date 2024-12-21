def process_file(input_file, output_file):
    # Обработка файла без использования дополнительных массивов
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        buffer = ""
        position = infile.seek(0, 2)  # Перемещаем указатель в конец файла
        while position > 0:
            position -= 1
            infile.seek(position)
            char = infile.read(1)

            if char == '.' and buffer:
                outfile.write(buffer[::-1] + '\n')
                buffer = ""
            else:
                buffer += char.strip()
