N = int(input())
dp = [0] * (N + 1)

for i in range(1, N + 1):
    cost, _, *prev = map(int, input().split())
    dp[i] = cost
    for j in prev:
        dp[i] = max(dp[i], dp[j] + cost)

print(max(dp))