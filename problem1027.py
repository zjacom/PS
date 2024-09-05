import sys

N = int(input())

buildings = list(map(int, input().split()))

m = [0] * N

for i in range(N - 1):
    max_slope = -sys.maxsize
    for j in range(i + 1, N):
        slope = (buildings[i] - buildings[j]) / (i - j)
        if slope <= max_slope:
            continue
        m[i] += 1
        m[j] += 1
        max_slope = slope

print(max(m))