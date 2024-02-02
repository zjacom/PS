# 조합
import sys
input = sys.stdin.readline

# input
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = []

# logic
def recur(num):
    if len(result) == M:
        print(' '.join(map(str, result)))
        return

    for i in range(num, len(arr)):
        result.append(arr[i])
        recur(i + 1)
        result.pop()

# output
recur(0)