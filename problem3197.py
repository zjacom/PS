import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())
dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]

arr1, arr2 = set(), set()
swans = []
for y in range(R):
    value = input().strip()
    temp = []
    for x, v in enumerate(value):
        if v == "L":
            swans.append((y, x))
        elif v == ".":
            arr2.add((y, x))

def melting():
    

def check():
    arr1 = arr1.union(arr2)
    if bfs():
        print(count)
        exit(0)
    else:


def bfs():
    q = deque([(swans[0][0], swans[0][1])])
    visited = [[False] * C for _ in range(R)]
    visited[swans[0][0]][swans[0][1]] = True

    while q:
        cy, cx = q.popleft()
        if cy == swans[1][0] and cx == swans[1][1]:
            return True

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < R and 0 <= nx < C:
                if (ny, nx) in arr1 and not visited[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = True



print(bfs())