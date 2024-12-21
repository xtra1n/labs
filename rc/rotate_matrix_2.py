def main():
    with open('in.txt', 'r') as in_file, open('out.txt', 'a+') as out_file:
        for i in range(len(in_file.readline().split())):
            in_file.seek(0)
            string = ''
            for k in in_file:
                string += k.split()[i] + ' '
            
            out_file.write(string[::-1] + '\n')


if __name__ == '__main__':
    main()