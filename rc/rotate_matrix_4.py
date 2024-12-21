with open("task5/in.txt", "r+", encoding="utf-8") as f, open("task5/out.txt", "a", encoding = "utf-8") as o:
    l = len(f.readline()) + 1
    f.seek(0)
    for i in range(0, l, 2):
        current = 0
        temp = []
        for j in range(l//2):
            f.seek(current*l + i)
            char = f.read(1)
            if char != "\n" and char != "":
                temp.append(char)
                current += 1
        if len(temp) > 0:
            o.write(" ".join(temp[::-1])+'\n')
