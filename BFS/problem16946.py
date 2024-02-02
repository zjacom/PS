from collections import deque, defaultdict
import copy
import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
dy, dx = [0, 0, -1, 1], [1, -1, 0, 0]
graph = []
for _ in range(N):
    graph.append(list(map(int, input().strip())))
result = copy.deepcopy(graph)

dic = defaultdict(int)

# 그룹 생성
def func(y, x, n):
    global graph
    q = deque([(y, x)])
    graph[y][x]= n
    while q:
        dic[n] += 1
        cy, cx = q.popleft()
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] == 0:
                q.append((ny, nx))
                graph[ny][nx] = n

def bfs(y, x):
    global graph
    temp, cnt = set(), 0
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] != 1:
            temp.add(graph[ny][nx])
    for c in temp:
        cnt += dic[c]
    return (cnt + 1) % 10



order = 1
for y in range(N):
    for x in range(M):
        if graph[y][x] == 0:
            order += 1
            func(y, x, order)

for y in range(N):
    for x in range(M):
        if result[y][x] == 1:
            result[y][x] = bfs(y, x)

for row in result:
    print(''.join([str(i) for i in row]))
