# 10942번
N = int(input())
arr = list(map(int, input().split()))

M = int(input())
answer = []
for _ in range(M):
    a, b = map(int, input().split())
    answer.append((a, b))

dp = [[0] * N for _ in range(N)]
for i in range(N):
    dp[i][i] = 1

for x in range(1, N):
    for y in range(x):
        if arr[x] == arr[y]:
            dp[y][x] = dp[y + 1][x - 1]
        if x - y == 1 and arr[x] == arr[y]:
            dp[y][x] = 1

for y, x in answer:
    print(dp[y - 1][x - 1])