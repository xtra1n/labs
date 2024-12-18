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


def arithmetic_expressions(x):
    for i in range(len(x)):
        line = list(x[i])
        j = 0
        while j < len(line):
            if line[j] == "+":
                number1 = ""
                cnt1 = 0
                flag = True
                for k in range(j - 1, -1, -1):
                    if line[k] == " " and flag:
                        cnt1 += 1
                    elif line[k].isdigit():
                        flag = False
                        number1 = line[k] + number1
                        cnt1 += 1
                    else:
                        break
                number2 = ""
                cnt2 = 0
                flag = True
                for k in range(j + 1, len(line)):
                    if line[k] == " " and flag:
                        cnt2 += 1
                    elif line[k].isdigit():
                        flag = False
                        number2 += line[k]
                        cnt2 += 1
                    else:
                        break
                if number1 != "" and number2 != "":
                    number1 = int(number1)
                    number2 = int(number2)
                    summa = number1 + number2
                    line[j] = summa
                    del line[j - cnt1:j + cnt2 + 1]
                    line.insert(j - cnt1, str(summa))
                    x[i] = "".join(line)
                else:
                    j += 1
            elif line[j] == "*":
                number1 = ""
                cnt1 = 0
                flag = True
                for k in range(j - 1, -1, -1):
                    if line[k] == " " and flag:
                        cnt1 += 1
                    elif line[k].isdigit():
                        flag = False
                        number1 = line[k] + number1
                        cnt1 += 1
                    else:
                        break
                number2 = ""
                cnt2 = 0
                flag = True
                for k in range(j + 1, len(line)):
                    if line[k] == " " and flag:
                        cnt2 += 1
                    elif line[k].isdigit():
                        flag = False
                        number2 += line[k]
                        cnt2 += 1
                    else:
                        break
                if number1 != "" and number2 != "" and number2 != "0":
                    number1 = int(number1)
                    number2 = int(number2)
                    summa = number1 * number2
                    line[j] = summa
                    del line[j - cnt1:j + cnt2 + 1]
                    line.insert(j - cnt1, str(summa))
                    x[i] = "".join(line)
                else:
                    j += 1
            else:
                j += 1
    return x


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
