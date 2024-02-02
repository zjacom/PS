import sys
input = sys.stdin.readline

# input
N, K = map(int, input().split())
temps = list(map(int, input().split()))
prefix = [0] * (N + 1)

# logic
for i in range(N):
    prefix[i + 1] = prefix[i] + temps[i]

maxi = -sys.maxsize
for i in range(K, N + 1):
    maxi = max(maxi, prefix[i] - prefix[i - K])

# output
print(maxi)