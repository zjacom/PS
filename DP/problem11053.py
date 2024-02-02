import sys
input = sys.stdin.readline

# input
N = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(N)]

# logic
for idx in range(1, N):
    for jdx in range(idx):
        if arr[idx] > arr[jdx]:
            dp[idx] = max(dp[idx], dp[jdx] + 1)

# output
print(max(dp))
