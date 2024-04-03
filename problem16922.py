N = int(input())

arr = [1, 5, 10, 50]

memo = [[set() for _ in range(4)] for _ in range(N)]

for i in range(4):
    memo[0][i].add(arr[i])


for y in range(1, N):
    for x in range(4):
        for num1 in memo[y - 1][x]:
            for i in range(4):
                memo[y][x].add(num1 + arr[i])

answer = set()

for i in range(4):
    answer = answer | memo[N - 1][i]

print(len(answer))