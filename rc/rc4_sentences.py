def process_file(input_file, output_file):
    # Буфер для хранения предложений
    sentences = []

    # Читаем входной файл построчно
    with open(input_file, 'r', encoding='utf-8') as infile:
        buffer = ""
        for line in infile:
            # Удаляем перевод строки и добавляем к буферу
            buffer += line.strip()
            
            # Разбиваем на предложения
            while '.' in buffer:
                sentence, buffer = buffer.split('.', 1)
                sentences.append(sentence.strip() + '.')

    # Обрабатываем остаток в буфере (если есть)
    if buffer.strip():
        sentences.append(buffer.strip() + '.')

    # Записываем предложения в обратном порядке в выходной файл
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for sentence in reversed(sentences):
            outfile.write(sentence + '\n')

# Пример использования:
process_file('in.txt', 'out.txt')
