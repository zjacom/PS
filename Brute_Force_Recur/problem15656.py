# 중복 있는 순열
import sys
input = sys.stdin.readline

# input
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = []

# logic
def recur():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return

    for i in range(len(arr)):
        result.append(arr[i])
        recur()
        result.pop()

# output
recur()