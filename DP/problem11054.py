import sys
input = sys.stdin.readline

# input
N = int(input())
arr = list(map(int, input().split()))
inc_dp = [1] * N
dec_dp = [1] * N

# logic
for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            inc_dp[i] = max(inc_dp[i], inc_dp[j] + 1)

arr = arr[::-1]
for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            dec_dp[i] = max(dec_dp[i], dec_dp[j] + 1)

maxi = 0
dec_dp = dec_dp[::-1]
for i in range(N):
    maxi = max(maxi, inc_dp[i] + dec_dp[i])

print(maxi - 1)