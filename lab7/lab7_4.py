from datetime import datetime

arr = list(map(str, input().split()))

start_time = datetime.now()

vowels_upper = 'AEIOU'


for i in range(len(arr)):
    for symbol in vowels_upper:
        arr[i] = arr[i].replace(symbol, symbol.lower())

print(arr)

end_time = datetime.now()
execution_time = end_time - start_time
print(f"Время выполнения: {execution_time}")