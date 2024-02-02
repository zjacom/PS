import sys
input = sys.stdin.readline

# input
n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [[] * n for _ in range(n)]

# logic
for i in range(n):
    if i == 0:
        dp[i].append(arr[i][0])
    elif i == 1:
        dp[i].append(dp[i - 1][0] + arr[i][0])
        dp[i].append(dp[i - 1][0] + arr[i][1])
    else:
        dp[i].append(dp[i - 1][0] + arr[i][0])
        for j in range(1, i):
            dp[i].append(max(dp[i - 1][j - 1] + arr[i][j], dp[i - 1][j] + arr[i][j]))
        dp[i].append(dp[i - 1][i - 1] + arr[i][i])

# output
print(max(dp[-1]))