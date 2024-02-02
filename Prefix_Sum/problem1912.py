import sys
input = sys.stdin.readline

# input
N = int(input())
arr = list(map(int, input().split()))
prefix = [0 for _ in range(N + 1)]

# logic
for i in range(N):
    prefix[i + 1] = max(prefix[i] + arr[i], arr[i])

# output
print(max(prefix[1:]))
