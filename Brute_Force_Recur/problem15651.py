import sys
input = sys.stdin.readline

# input
N, M = map(int, input().split())
result = []

# logic
def recur():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    for i in range(1, N + 1):
        result.append(i)
        recur()
        result.pop()

# output
recur()
