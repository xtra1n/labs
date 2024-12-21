def main():
    with open('/home/andrey/pyprojects/labs/in2.txt', 'r') as infile, open('out.txt', 'w') as outfile:
        buffer = ''
        
        # Обработка файла построчно
        for line in infile:
            buffer += line.strip()  # Сохраняем текущую строку в буфере
            sentences = buffer.split('.')
            
            # Записываем предложения в обратном порядке
            for sentence in reversed(sentences[:-1]):
                if sentence.strip():
                    outfile.write(sentence.strip() + '.\n')
            
            buffer = sentences[-1]  # Оставляем остаток для следующей строки

        # Если в конце есть неполное предложение в buffer, записываем его
        if buffer.strip():
            outfile.write(buffer.strip() + '.\n')

if __name__ == '__main__':
    main()
