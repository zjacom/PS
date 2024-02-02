import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dirY = [-1, 1, 0, 0]
dirX = [0, 0, -1, 1]

def dfs(y, x):
    global map_, answer, M
    map_[y][x] = False

    if y == M:
        answer = True
        return

    for i in range(4):
        newY = y + dirY[i]
        newX = x + dirX[i]
        if map_[newY][newX]:
            dfs(newY, newX)


M, N = map(int, input().split())
MAX = 1000 + 10
map_ = [[False] * MAX for _ in range(MAX)]

for i in range(1, M + 1):
    row = input()
    for j in range(1, N + 1):
        map_[i][j] = (row[j - 1] == "0")


answer = False
for j in range(1, N + 1):
    if map_[1][j]:
        dfs(1, j)

print("YES" if answer else "NO")
