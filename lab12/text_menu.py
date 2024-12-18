from text_editor import left_alignment, right_alignment, justify_alignment, \
    remove_word, replace_word, arithmetic_expressions, process_text
from text import get_text
from utils import output


def menu():
    text = get_text()
    output(text)
    output_menu()

    while True:
        try:
            point = int(input('\nВведите номер пункта: '))
            if point == 1:
                text = left_alignment(text)
                output(text)
                output_menu()
            if point == 2:
                text = right_alignment(text)
                output(text)
                output_menu()
            if point == 3:
                text = justify_alignment(text)
                output(text)
                output_menu()
            if point == 4:
                word = input('Введите слово для замены: ')
                text = remove_word(text, word)
                output(text)
                output_menu()
            if point == 5:
                word = input('Введите слово для замены: ')
                new_word = input('Введите слово на которое заменить: ')
                text = replace_word(text, word, new_word)
                output(text)
                output_menu()
            if point == 6:
                text = arithmetic_expressions(text)
                output(text)
                output_menu()
            if point == 7:
                text = process_text(text)
                output(text)
                output_menu()
            if point == 0:
                return

        except Exception as e:
            print('Ой!', e)

def output_menu():
        print('\nВыберите пункт меню:\n'
          '\n1. Выровнять текст по левому краю.\n'
          '2. Выровнять текст по правому краю.\n'
          '3. Выровнять текст по ширине.\n'
          '4. Удаление всех вхождений заданного слова.\n'
          '5. Замена одного слова другим во всём тексте.\n'
          '6. Вычисление арифметических выражений над целыми числами\n'
          '7. Найти и удалить предложение в котором больше всего слов\n'
          '0. Выход')