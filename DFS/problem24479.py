import collections
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph_dfs = collections.defaultdict(list)
visited = [False] * (N + 1)
order_list = [0] * (N + 1)
order = 1

for _ in range(M):
    x, y = map(int, input().split())
    graph_dfs[x].append(y)
    graph_dfs[y].append(x)


for i in list(graph_dfs.keys()):
    graph_dfs[i].sort()


def dfs(node):
    global order, order_list, visited, graph_dfs
    visited[node] = True
    order_list[node] = order
    order += 1

    for n in graph[node]:
        if not visited[n]:
            dfs(n)


dfs(R)
for i in range(1, N + 1):
    print(order_list[i])
