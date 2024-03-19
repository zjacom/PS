N = int(input())
arr = list(map(int, input().split()))

M = int(input())
answer = []
for _ in range(M):
    S, E = map(int, input().split())
    answer.append((S, E))

dp = [[0] * N for _ in range(N)]

for x in range(N):
    for y in range(x + 1):
        if y - x == 0:
            dp[y][x] = 1
        elif x - y == 1:
            if arr[x] == arr[y]:
                dp[y][x] = 1
        elif arr[x] == arr[y]:
            dp[y][x] = dp[y + 1][x - 1]

for y, x in answer:
    print(dp[y - 1][x - 1])