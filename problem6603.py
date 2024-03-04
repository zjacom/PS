from itertools import combinations

arr = []
answer = []
while True:
    line = input().strip()
    if line == '0':
        break
    arr.append(list(map(int, line.split())))

for idx in range(len(arr)):
    li = list(combinations(arr[idx][1:], 6))
    for num in li:
        print(num)
    if idx != len(arr) - 1:
        print()
