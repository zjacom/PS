from collections import defaultdict
from itertools import permutations

N = int(input())

graph = defaultdict(list)

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
visited[1] = True

right = list(map(int, input().split()))

def dfs(node, path):
    visited[node] = True
    path.append(node)

    if node in path:
        return
    if len(path) > N:
        return
    if len(path) == N:
        print(path)
        return

    if len(graph[node]) == 1 and not visited[graph[node][0]]:
        dfs(graph[node][0], path)
        visited[graph[node][0]] = False
    elif len(graph[node]) > 1:
        for arr in list(permutations(graph[node], len(graph[node]))):
            for nxt in arr:
                if not visited[nxt]:
                    dfs(nxt, path)
                    visited[nxt] = False

dfs(1, [])