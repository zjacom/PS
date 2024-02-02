import sys
input = sys.stdin.readline

# input
N, M = map(int, input().split())
result = []

# logic
def recur(num):
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    for i in range(num, N + 1):
        result.append(i)
        recur(i)
        result.pop()

# output
recur(1)
