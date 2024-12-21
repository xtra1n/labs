def main():
    with open('in.txt', 'r') as infile, open('out.txt', 'w') as outfile:
        for line in infile:
            start = 0
            finish = 0
            for el in line:
                finish += 1
                if el == '.':
                    outfile.write(line[start:finish].strip() + '\n')
                    start = finish
            k = line[-1][-1]
            if line[-2][-1] == '.':
                outfile.write(line[start:finish].strip())
            else:
                    outfile.write(line[start:finish].strip() + ' ')


if __name__ == '__main__':
    main()