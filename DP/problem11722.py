import sys
input = sys.stdin.readline

# input
N = int(input())
arr = list(map(int, input().split()))[::-1]
dp = [1] * N

# logic
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# output
print(max(dp))