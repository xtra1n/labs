arr = list(map(int, input().split()))

ind_plus = 1
ind_minus = 0

for i in range(len(arr)):
    if arr[i] <= 0:
        arr[ind_minus] = arr[i]
        ind_minus += 1
    else:
        ind_plus += 1

print(arr)

if ind_plus != 1:
    arr = arr[:ind_minus]

print(arr, ind_plus, ind_minus)
