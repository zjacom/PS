import sys
input = sys.stdin.readline

# input
N = int(input())
dp = [[0] * 2 for _ in range(100_000 + 1)]

# logic
dp[1][0], dp[1][1] = 1, 2


for i in range(2, 100_000 + 1):
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) % 9901
    dp[i][1] = ((2 * dp[i - 1][0]) + dp[i - 1][1]) % 9901

# output
print(sum(dp[N]) % 9901)