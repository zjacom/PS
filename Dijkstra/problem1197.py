import heapq
from collections import defaultdict

V, E = map(int, input().split())
graph = defaultdict(list)
for _ in range(E):
    a, b, w = map(int, input().split())
    graph[a].append((w, b))
    graph[b].append((w, a))

q = [(0, 1)]
visited = [False] * (V + 1)
count, answer = 0, 0

while q:
    if count == V:
        break
    weight, node = heapq.heappop(q)

    if not visited[node]:
        visited[node] = True
        count += 1
        answer += weight
        for nxt in graph[node]:
            heapq.heappush(q, nxt)

print(answer)