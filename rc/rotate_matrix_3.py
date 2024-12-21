f_in = open('in.txt')
f_out = open('out.txt','w+')

col_num = len(f_in.readline().split())
for i in range(col_num - 1):
    f_in.seek(0)
    string = []
    for k in f_in:
        string.append(k.split()[i])
    f_out.write(' '.join(string[::-1]) + '\n')
f_in.seek(0)
string = []
for k in f_in:
    string.append(k.split()[col_num - 1])
f_out.write(' '.join(string[::-1]))

f_in.close()
f_out.close()
