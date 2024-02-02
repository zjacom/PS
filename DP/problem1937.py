import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# input
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [[0] * N for _ in range(N)]
dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]

def recur(y, x):
    global arr
    if dp[y][x]: return dp[y][x]

    temp = 0
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if arr[y][x] < arr[ny][nx]:
                temp = max(temp, recur(ny, nx) + 1)
                dp[y][x] = temp
    return dp[y][x]

for y in range(N):
    for x in range(N):
        recur(y, x)

result = 0
for row in dp:
    result = max(result, max(row))

print(result + 1)
