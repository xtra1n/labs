arr = list(map(str, input().split()))

flag = any(i.isdigit() for i in arr)
result = 'Не нашлось такого элемента'
max_len = -1

for el in arr:
    if ( (not(any((char.isdigit()) for char in el))) and
        (len(el) > max_len)):
        result = el
        max_len = len(el)



print(result)