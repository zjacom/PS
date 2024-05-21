# 2252번
from collections import defaultdict, deque

N, M = map(int, input().split())
graph = defaultdict(list)
indegrees = [0] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    indegrees[b] += 1
    graph[a].append(b)

q = deque()
for i in range(1, N + 1):
    if indegrees[i] == 0:
        q.append(i)

result = []
while q:
    node = q.popleft()
    result.append(node)
    for nxt in graph[node]:
        indegrees[nxt] -= 1
        if indegrees[nxt] == 0:
            q.append(nxt)

print(*result)