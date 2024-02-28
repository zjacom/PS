import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())
swan = []
main, temp, calc = set(), set(), set()
dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
count = 0
for y in range(R):
    value = input().strip()
    for x, v in enumerate(value):
        if v == "L":
            swan.append((y, x))
            temp.add((y, x))
            main.add((y, x))
        elif v == ".":
            temp.add((y, x))
            main.add((y, x))

def melting():
    global count, temp, main
    calc = set()
    calc = calc.union(temp)
    temp = set()
    count += 1
    for cy, cx in calc:
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < R and 0 <= nx < C:
                temp.add((ny, nx))
                main.add((ny, nx))


def bfs():
    q = deque([(swan[0][0], swan[0][1])])
    visited = [[False] * C for _ in range(R)]
    visited[swan[0][0]][swan[0][1]] = True

    while q:
        cy, cx = q.popleft()
        if cy == swan[1][0] and cx == swan[1][1]:
            return True
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if (ny, nx) in main:
                if not visited[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = True

while not bfs():
    melting()

print(count)