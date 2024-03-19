import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())

arr = list(map(int, input().split()))

dp = [sys.maxsize] * len(arr)

def recur(idx):
    if dp[idx] != sys.maxsize:
        return dp[idx]
    if idx == N - 1:
        return 0
    for nxt in range(1, arr[idx] + 1):
        if idx + nxt < N:
            dp[idx] = min(dp[idx], recur(idx + nxt) + 1)
    
    return dp[idx]

if N == 1:
    print(0)
    exit(0)
recur(0)
print(dp[0]) if dp[0] != sys.maxsize else print(-1)