from collections import deque
import sys
input = sys.stdin.readline

# 입력
wall = []
graph = [[] for _ in range(8)]
for y in range(8):
    value = input().strip()
    for x, v in enumerate(value):
        if v == "#":
            graph[y].append("#")
            wall.append([y, x])
        else:
            graph[y].append(".")

dy, dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1] , [-1, 0, 1, 1, -1, 0, 1, -1, 0]

# 로직
def bfs():
    global graph
    q = deque([(7, 0)])
    while q:
        for _ in range(len(q)):
            cy, cx = q.popleft()
            if [cy, cx] in wall:
                continue
            if cy == 0:
                return 1
            for i in range(8):
                ny, nx = cy + dy[i], cx + dx[i]
                if 0 <= ny < 8 and 0 <= nx < 8:
                    if [ny, nx] not in wall:
                        q.append((ny, nx))
        
        for i in range(len(wall)):
            wall[i] = [wall[i][0] + 1, wall[i][1]]
    return 0


# 출력
if len(wall) == 0:
    print(1)
else:
    print(bfs())
