import sys
input = sys.stdin.readline

# input
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [1 for _ in range(N)]

arr = sorted(arr, key=lambda x : x[0])

# logic
for i in range(1, N):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[j] + 1, dp[i])

# output
print(N - max(dp))
print(dp)