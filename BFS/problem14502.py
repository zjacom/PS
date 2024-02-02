import copy
from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline
dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]

# 입력
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
able = []
v = deque()

for y in range(N):
    for x in range(M):
        if graph[y][x] == 0:
            able.append((y, x))
        if graph[y][x] == 2:
            v.append((y, x))

combi = list(combinations(able, 3))

# 로직
def bfs(wall, virus, g):
    cp = [row[:] for row in g]
    cv = copy.deepcopy(virus)

    for y, x in wall:
        cp[y][x] = 1
    
    while cv:
        cy, cx = cv.popleft()
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < N and 0 <= nx < M and cp[ny][nx] == 0:
                cp[ny][nx] = 2
                cv.append((ny, nx))
    return cp

# 출력
answer = 0
for c in combi:
    count = 0
    new_g = bfs(c, v, graph)
    for row in new_g:
        count += row.count(0)
    answer = max(answer, count)

print(answer)
