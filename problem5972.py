from collections import defaultdict
import heapq
import sys

N, M = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

q = []
heapq.heappush(q, (0, 1))
visited = [sys.maxsize] * (N + 1)
visited[1] = 0

while q:
    cost, node = heapq.heappop(q)

    if node == N:
        print(cost)
        break

    for nxt, c in graph[node]:
        if visited[nxt] > cost + c:
            heapq.heappush(q, (cost + c, nxt))
            visited[nxt] = cost + c
        