N = int(input())
dp = [0] * (N + 1)

for i in range(1, N + 1):
    cost, *prev = map(int, input().split())
    maxi = 0
    for j in prev[1:]:
        maxi = max(maxi, dp[j])
    dp[i] = cost + maxi

print(max(dp))