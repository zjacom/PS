import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

result = []
MAX = 50 + 10
w, h = MAX, MAX

dirY = [1, -1, 0, 0, 1, 1, -1, -1]
dirX = [0, 0, 1, -1, -1, 1, 1, -1]


def dfs(y, x):
    global graph
    graph[y][x] = False

    for i in range(8):
        newY = y + dirY[i]
        newX = x + dirX[i]
        if graph[newY][newX]:
            dfs(newY, newX)


while True:
    w, h = map(int, input().split())
    graph = [[False] * MAX for _ in range(MAX)]

    if w == 0 and h == 0:
        break

    for y in range(1, h + 1):
        row = list(map(int, input().split()))
        for x in range(1, w + 1):
            graph[y][x] = (row[x - 1] == 1)

    count = 0
    for y in range(1, h + 1):
        for x in range(1, w + 1):
            if graph[y][x]:
                dfs(y, x)
                count += 1

    result.append(count)

for cnt in result:
    print(cnt)
