from collections import deque, defaultdict

N, M = map(int, input().split())

indegrees = [0] * (N + 1)

graph = defaultdict(list)
order = []

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegrees[b] += 1

q = deque()
for i, v in enumerate(indegrees):
    if v == 0 and i != 0:
        q.append(i)

while q:
    node = q.popleft()
    order.append(node)

    for nxt in graph[node]:
        indegrees[nxt] -= 1
        if indegrees[nxt] == 0:
            q.append(nxt)

print(*order)