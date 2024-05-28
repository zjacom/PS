N = int(input())

arr = []

for _ in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))

result = []
for i in range(N):
    new_arr = arr[:i] + arr[i + 1:]
    x, y = arr[i][0], arr[i][1]

    cnt = 1
    for a, b in new_arr:
        if a > x and b > y:
            cnt += 1
    
    result.append(cnt)

print(*result)