arr = list(map(int, input().split()))

cnt = 0

for el in arr:
    if el % 2 != 0:
        cnt += 1
        arr.append(0)

n = len(arr) - 1
for i in range(len(arr) - cnt - 1, -1, -1):
    if arr[i] % 2 != 0:
        arr[n - 1], arr[n] = arr[i], 2 * arr[i]
        print(n)
        n-=2
    else:
        arr[n] = arr[i] 
        n-=1

        

print(arr)