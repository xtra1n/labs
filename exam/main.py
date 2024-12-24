import re


def split_sentences(in_file, out_file):
    with open(in_file, 'r') as in_file, open(out_file, 'w') as out_file:
        buffer = ''
        for line in in_file:
            buffer += line.strip()
            sentences = buffer.split('.')
            for sentence in sentences[:-1]:
                sentence = replace_num(sentence)
                out_file.write(sentence.strip() + '.\n')
            buffer = sentences[-1]


def replace_num(sentence):
    sentence = re.sub(r'[+-]?([0-9a-fA-F]+\,+([0-9A-Fa-f]))', convert_hex, sentence)
    return sentence

def hex_to_oct(num, is_digit):
    num = bin(int(num, 16))[2:]
    num = '0' * (4 - len(num)) + num
    length = len(num)
    if is_digit:
        num = num + '0' * (3 - (length % 3))
    else:
        num = '0' * (3 - (length % 3)) + num
    num = ''.join(oct(int(num[i:i+3], 2))[2:] for i in range(0, len(num), 3) )
    return num


def convert_hex(match):
    num = match.group(0)
    main_part = num.split(',')[0]
    digit = num.split(',')[1]
    main_part = hex_to_oct(main_part, 0)
    digit = hex_to_oct(digit, 1)

    return main_part + ',' + digit


def main():
    in_file = 'in.txt'
    out_file = 'out.txt'
    split_sentences(in_file, out_file)


if __name__ == '__main__':
    main()