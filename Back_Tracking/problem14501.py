import sys
sys.setrecursionlimit(10**6)

# input
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

result = -sys.maxsize

# logic
def recur(idx, benefit):
    global result
    if idx > N:
        return

    if idx == N:
        result = max(result, benefit)
        return
    
    recur(idx + 1, benefit)
    recur(idx + arr[idx][0], benefit + arr[idx][1])

# output
recur(0, 0)
print(result)