import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# input
N = int(input())
dp = [sys.maxsize] * (N + 1)

# logic
def recur(num):    
    if num == 1:
        return 0
    
    if dp[num] != sys.maxsize:
        return dp[num]
    
    if num % 3 == 0 and num % 2 == 0:
        dp[num] = min(recur(num // 3) + 1, recur(num // 2) + 1)
    elif num % 3 == 0:
        dp[num] = min(recur(num // 3) + 1, recur(num - 1) + 1)
    elif num % 2 == 0:
        dp[num] = min(recur(num // 2) + 1, recur(num - 1) + 1)
    else:
        dp[num] = recur(num - 1) + 1
    
    return dp[num]

# oupput
if N == 1:
    print(0)
else:
    recur(N)
    print(dp[-1])