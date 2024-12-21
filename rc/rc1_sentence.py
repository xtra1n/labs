def main():
    with open('/home/andrey/pyprojects/labs/in2.txt', 'r') as infile, open('out.txt', 'w') as outfile:
        buffer = ''
        for line in infile:
            buffer += line.strip()
            sentences = buffer.split('.')
            for sentence in sentences[:-1]:
                if sentence.strip():
                    outfile.write(sentence + '.\n')
            buffer = sentences[-1]

if __name__ == '__main__':
    main()