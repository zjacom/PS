import collections

N, M, V = map(int, input().split())
graph = collections.defaultdict(list)
visited = [False] * (N + 1)


for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for key in list(graph.keys()):
    graph[key].sort()


def dfs(node):
    visited[node] = True
    print(node, end=' ')

    for n in graph[node]:
        if not visited[n]:
            dfs(n)


def bfs(node):
    visited[node] = True
    queue = [node]

    while queue:
        n = queue.pop(0)
        print(n, end=' ')
        for i in graph[n]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(V)
print()
visited = [False] * (N + 1)
bfs(V)