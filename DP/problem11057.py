import sys
input = sys.stdin.readline

# input
N = int(input())
dp = [[0] * (10) for _ in range(N + 1)]

# logic
for i in range(10):
    dp[1][i] = 1

for y in range(2, N + 1):
    for x in range(10):
        for r in range(x + 1):
            dp[y][x] += (dp[y - 1][r] % 10_007)

# output
print(sum(dp[N]) % 10_007)
