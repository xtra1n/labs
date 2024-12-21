import struct

record_size = struct.calcsize('q')


def main():
    n = [9, 23, 121, 64, 1, 0, -10]
    with open('numbers.bin', 'w+b') as file:
        for i in n:
            record = struct.pack('q', i)
            file.write(record)

    with open('numbers.bin', 'r+b') as file:
        file.seek(0,2)
        file_size = file.tell()
        n = file_size // record_size
        for i in range(n):
            for j in range(n-i-1):
                file.seek(j*record_size)
                a_b = file.read(record_size)
                file.seek((j+1)*record_size)
                b_b = file.read(record_size)

                a = struct.unpack('q', a_b)[0]
                b = struct.unpack('q', b_b)[0]
                if a > b:
                    file.seek(j*record_size)
                    file.write(struct.pack('q', b))
                    file.seek((j+1)*record_size)
                    file.write(struct.pack('q', a))

    with open('numbers.bin', 'rb') as file:
        while line := file.read(record_size):
            line = struct.unpack('q', line)
            line = line[0]
            print(line)

if __name__ == '__main__':
    main()