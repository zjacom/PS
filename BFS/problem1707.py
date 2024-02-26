import sys
input = sys.stdin.readline
from collections import defaultdict, deque

# input
K = int(input())
result = []

def bfs(node):
    global temp, graph, visited

    q = deque([node])
    visited[node] = 1

    while q:
        n = q.popleft()

        for nxt in graph[n]:
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt] = -visited[n]
            elif visited[n] == visited[nxt]:
                return True


for idx in range(K):
    V, E = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [0] * (V + 1)
    temp = "YES"
    for i in range(1, V + 1):
        if not visited[i]:
            if bfs(i):
                temp = "NO"
                break
    result.append(temp)

for r in result:
    print(r)