import sys
sys.setrecursionlimit(10 ** 6)

from copy import deepcopy

N = int(input())

dirP = ([1, 1], [0, 1], [-1, 1], [1, -1], [0, -1], [1, 0], [-1, 0], [-1, -1])
answer = 0

def recur(y, x, visited, count):
    global answer
    visited[y][x] = 1
    if count == 0:
        answer += 1
        return
    for i in range(1, N):
        for dy, dx in dirP:
            ny, nx = y + dy * i, x + dx * i
            if 0 <= ny < N and 0 <= nx < N:
                visited[ny][nx] = 1
    temp = deepcopy(visited)
    for a in range(N):
        for b in range(N):
            if not visited[a][b]:
                recur(a, b, visited, count - 1)
                visited = temp

for y in range(N):
    for x in range(N):
        visited = [[0] * N for _ in range(N)]
        recur(y, x, visited, N)

print(answer)