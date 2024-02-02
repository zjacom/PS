import sys
input = sys.stdin.readline

# input
N = int(input())

dp = [0] * (30 + 1)
dp[2] = 3

# logic
for idx in range(4, 30 + 1, 2):
    dp[idx] += (3 * dp[idx - 2]) + 2
    for jdx in range(0, idx - 2, 2):
        dp[idx] += (2 * dp[jdx])

# output
print(dp[N])