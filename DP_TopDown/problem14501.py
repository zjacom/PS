import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# input
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
dp = [0 for _ in range(N)]

# logic
def recur(idx):
    global arr, dp
    if idx > N:
        return -sys.maxsize
    if idx == N:
        return 0
    
    if dp[idx]:
        return dp[idx]
    
    dp[idx] = max(recur(idx + arr[idx][0]) + arr[idx][1], recur(idx + 1))

    return dp[idx]

# output
print(recur(0))