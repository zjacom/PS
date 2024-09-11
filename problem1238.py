import sys
from collections import defaultdict, deque

N, M, X = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))

costs = [0] * (N + 1)

def bfs(src, dst):
    q = deque([(src, 0)])
    visited = [sys.maxsize] * (N + 1)
    visited[src] = 0

    while q:
        s, c = q.popleft()

        for nxt, nc in graph[s]:
            if visited[nxt] > c + nc:
                q.append((nxt, c + nc))
                visited[nxt] = c + nc
    
    return visited[dst]

for i in range(1, N + 1):
    costs[i] = bfs(i, X)

for i in range(1, N + 1):
    costs[i] += bfs(X, i)

print(max(costs))
        