import sys
input = sys.stdin.readline

# input
n = int(input())

# logic
dp = [1] * (1000 + 1)
for i in range(2, 1000 + 1):
    dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 10_007

# output
print(dp[n])