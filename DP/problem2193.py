import sys
input = sys.stdin.readline

# input
N = int(input())
dp = [0] * (90 + 1)
dp[1], dp[2] = 1, 1

# logic
for i in range(3, 90 + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

# output
print(dp[N])

"""
import sys
input = sys.stdin.readline

# input
N = int(input())

# logic
dp = [[0] * 2 for _ in range(N + 1)]
dp[1][1] = 1

for i in range(2, N + 1):
    dp[i][0] = sum(dp[i - 1])
    dp[i][1] = dp[i - 1][0]

# output
print(sum(dp[N]))
"""