import sys
input = sys.stdin.readline

# input
n = int(input())
arr = list(map(int, input().split()))

# logic
dp = [[x for x in arr] for _ in range(2)] # dp[0]은 제거 안함, dp[1]은 제거함
dp[0][0] = arr[0]

for i in range(1, n):
    dp[0][i] = max(dp[0][i - 1] + arr[i], dp[0][i])
    dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + arr[i])

# output
print(max(max(dp[0]), max(dp[1])))