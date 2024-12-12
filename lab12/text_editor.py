import re


def left_alignment(text: list[str]) -> list[str]:
    for string_id in range(len(text)):
        text[string_id] = ' '.join(text[string_id].split())

    return text


def right_alignment(text: list[str]) -> list[str]:

    text = left_alignment(text)
    max_len = search_max_len(text)
    for string_id in range(len(text)):
        string_len = len(text[string_id])
        if string_len != max_len:
            text[string_id] = ' ' * (max_len - string_len) + text[string_id]

    return text


def justify_alignment(text: list[str]) -> list[str]:
    text = left_alignment(text)
    max_len = search_max_len(text)
    for string_id in range(len(text)):
        string_len = len(text[string_id])
        if string_len != max_len:
            words = text[string_id].split()
            if max_len - string_len >= len(words) - 1 and len(words) != 1:
                new_space_cnt = (max_len - string_len) // (len(words) - 1) + 1
            elif len(words) == 1:
                new_space_cnt = max_len - string_len
                space = ' ' * (new_space_cnt)
                words[0] = space + words[0]
            else:
                new_space_cnt = 1
            if len(words) != 1:
                extra_space_cnt = (max_len - string_len) % (len(words) - 1)
            else:
                extra_space_cnt = 0
            for i in range(1, len(words)):
                if i <= extra_space_cnt:
                    space = ' ' * (new_space_cnt + 1)
                    words[i] = space + words[i]
                else:
                    space = ' ' * (new_space_cnt)
                    words[i] = space + words[i]
            text[string_id] = ''.join(words)

    return text


def remove_word(text: list[str], word: str) -> list[str]:
    """
     Удаляем слово
    """
    for line_num in range(len(text)):
        words = text[line_num].split()
        for i in range(len(words)):
            if '.' in words[i] or ',' in words[i]:
                if word == words[i][:-1]:
                    text[line_num] = text[line_num].replace(f' {word}','')
            else:
                if word == words[i]:
                    text[line_num] = text[line_num].replace(f' {word}','').replace(f'{word} ','')
    return text


def replace_word(text: list[str], word: str, new_word: str) -> list[str]:
    """
    Замена слова
    """
    for line_num in range(len(text)):
        words = text[line_num].split()
        for i in range(len(words)):
            if '.' in words[i] or ',' in words[i]:
                if word == words[i][:-1]:
                    text[line_num] = text[line_num].replace(f' {word}',f' {new_word}')
            else:
                if word == words[i]:
                    text[line_num] = text[line_num].replace(f' {word}','').replace(f'{word} ',f' {new_word}')
    return text


def replace_arifmetic(text: list[str]):
    numbers = '0123456789'
    nums = []  # сюда сохраняем числа
    operators = []  # сюда сохраняем знаки сложения и умножения
    arifmetic_start = (-1, -1)
    new_num = ''
    arifmetic_end = (-1, -1)
    rows_to_delete = []  #  здесь храним индексы строк, которые нужно удалить
    wrong_operators = False  # флаг на случай, если перед оператором не было числа
    for i in range(len(text)):
        k = 0
        while k < len(text[i]):  # реализуем for через while (необходимо из-за удалений)
            letter = text[i][k]
            if letter != ' ':
                if letter in numbers:
                    if not new_num and not nums:  # если арифметическое выражение только началось
                        arifmetic_start = (i, k)
                    new_num += letter
                    arifmetic_end = (i, k)
                elif letter in '+*':
                    if new_num:  # если перед оператором было число
                        nums.append(int(new_num))  # сохраняем число
                        new_num = ''
                        operators.append(letter)  # сохраняем оператор
                    else:
                        wrong_operators = True  # <- перед оператором не было числа

                # если буква не является составляющей арифметического выражения или это последняя буква текста (вдруг выражение заканчивается в конце текста) или перед оператором не было числа
                if letter not in '+* ' + numbers or (i + 1 == len(text) and k + 1 == len(text[i])) or wrong_operators:
                    if new_num:
                        nums.append(int(new_num))
                    if nums and len(operators) == len(nums):  # если в конце арифметического выражения оказался оператор
                        operators = operators[:-1]
                    if len(nums) - 1 == len(operators) and operators:  # проверка верное ли количество операторов и есть ли они вообще
                        res = calculate(nums, operators)  # считаем значение выражения
                        row_ind = arifmetic_start[0]
                        if arifmetic_end[0] != arifmetic_start[0]:  # если в арифметическом выражении был переход строк (возможно больше одной)
                            text[row_ind] = text[row_ind][:arifmetic_start[1]] + f'{res:.3g}' + text[row_ind][len(text[arifmetic_start[0]]) + 1:]  # вставляем результат в начало арифм. выражения
                            text[i] = text[arifmetic_end[0]][arifmetic_end[1] + 1:]  # убираем конец выражения (который был на другой строке)
                            for d in range(arifmetic_start[0] + 1, arifmetic_end[0]):  # запоминаем все строки между первой строкой, где началось выражение и последней (если такие есть)
                                rows_to_delete.append(d)
                            k = 0  # возвращаемся в начало предложения, где закончилось выражение (до того как мы его удалили, оно было вначале)
                        else:  # если в арифметическом выражении не было перехода по строкам
                            text[row_ind] = text[row_ind][:arifmetic_start[1]] + f'{res:.3g}' + text[row_ind][arifmetic_end[1] + 1:]
                            k -= abs(len(str(res)) - (arifmetic_end[1] - arifmetic_start[1]))  # возвращаемся в конец результата, на который мы заменили выражение
                    nums = []
                    operators = []
                    new_num = ''
                    arifmetic_start = arifmetic_end = -1
                    wrong_operators = 0
            k += 1
    for d in rows_to_delete[::-1]:  # удаляем строки, которые запомнили
        del text[d]

    return text


def calculate(nums: list[str], operators: list[str]):
    """
    Считаем выражение
    """
    if '*' in operators:
        id_op = 0
        while id_op < len(operators):
            if operators[id_op] == '*':
                value = nums[id_op] * nums[id_op + 1]
                nums[id_op] = value
                del nums[id_op + 1]
                del operators[id_op]
            else:
                id_op += 1
    res = nums[0]
    if len(nums) > 1:
        for num in nums[1:]:
            res += num
    return res


def process_text(text: list[str]) -> tuple[str, list[str]]:
    longest_sentence = ''
    current_sentence = ''

    for line in text:
        for char in line:
            current_sentence += char
            if char in '.!?':
                if len(current_sentence) > len(longest_sentence):
                    longest_sentence = current_sentence.strip()
                current_sentence = ''
        if current_sentence:
            current_sentence += ' '

    words = [word.strip('.,!?;:') for word in longest_sentence.split()]
    words = [word for word in words if word]

    shortest_word = min(words, key=len)

    new_text = []

    for line in text:
        parts = line.split(' ')
        new_line_parts = []
        removed = False
        for part in parts:
            clean_part = part.strip('.,!?;:')
            if clean_part == shortest_word and not removed:
                removed = True
            else:
                new_line_parts.append(part)
        new_text.append(' '.join(new_line_parts))

    print('Короткое слово: ', shortest_word)

    return new_text


def search_max_len(text):
    """
    Ищем длинную строку
    """
    max_len = max(text, key=len)

    return len(max_len)
