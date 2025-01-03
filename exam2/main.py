def read_matrix():
    with open('C:\py\labs\exam2\in.txt', 'r') as f1, open('out.txt', 'w') as f2:
        for line in f1:
            for char in line:
                f2.seek(0, 0)
                print(char)
                f2.write(char + '\n')




def main():
    pass


if __name__ == '__main__':
    main()