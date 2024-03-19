N, S, M = map(int, input().split())
arr = list(map(int, input().split()))

dp = [{S}] + [set() for _ in range(N)]

for i in range(N):
    for j in dp[i]:
        if j + arr[i] <= M:
            dp[i + 1].add(j + arr[i])
        if j - arr[i] >= 0:
            dp[i + 1].add(j - arr[i])

print(max(dp[-1])) if dp[-1] else print(-1)