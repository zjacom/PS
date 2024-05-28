# 14263번
from collections import defaultdict
import heapq

N, M = map(int, input().split())

grid = [list(input()) for _ in range(N)]

dic = defaultdict(lambda: [M, 0, 0, N]) # left, right, down, up

for y in range(N):
    for x in range(M):
        if grid[y][x] != ".":
            card = grid[y][x]
            dic[card][0] = min(dic[card][0], x)
            dic[card][1] = max(dic[card][1], x)
            dic[card][2] = max(dic[card][2], y)
            dic[card][3] = min(dic[card][3], y)

indegrees = defaultdict(int)
graph = defaultdict(list)

for card, (left, right, down, up) in dic.items():
    for y in range(up, down + 1):
        for x in range(left, right + 1):
            if grid[y][x] == ".":
                print(-1)
                exit(0)
            if grid[y][x] != card and grid[y][x] not in graph[card]:
                indegrees[grid[y][x]] += 1
                graph[card].append(grid[y][x])

q = []

for card in dic.keys():
    if card not in indegrees:
        heapq.heappush(q, card)

order = []
while q:
    node = heapq.heappop(q)
    order.append(node)

    for nxt in graph[node]:
        indegrees[nxt] -= 1
        if indegrees[nxt] == 0:
            heapq.heappush(q, nxt)

if len(order) != len(dic):
    print(-1)
else:
    print(''.join(order))