import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# input
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

dp = [[0 for _ in range(n + 1)] for _ in range(3)]

# logic
for idx in range(1, n + 1):
    dp[0][idx] = max(dp[0][idx - 1], dp[1][idx - 1], dp[2][idx - 1])
    dp[1][idx] = max(dp[1][idx], dp[0][idx - 1] + arr[idx - 1])
    dp[2][idx] = max(dp[2][idx], dp[1][idx - 1] + arr[idx - 1])

# output
print(max(dp[0][n], dp[1][n], dp[2][n]))