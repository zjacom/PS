# 1027번
import sys

N = int(input())
buildings = list(map(int, input().split()))


def calc_lean(a, ah, b, bh):
    return (bh - ah) / (b - a)

dp = [0] * N

for a in range(N - 1):
    ah = buildings[a]
    max_lean = -sys.maxsize
    for b in range(a + 1, N):
        bh = buildings[b]
        lean = calc_lean(a, ah, b, bh)
        if lean > max_lean:
            dp[a] += 1
            dp[b] += 1
            max_lean = lean

print(max(dp))