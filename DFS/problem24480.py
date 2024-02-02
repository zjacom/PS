import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(idx):
    global visited, answer, order, graph_dfs
    visited[idx] = True
    answer[idx] = order
    order += 1

    for i in graph[idx]:
        if not visited[i]:
            dfs(i)


N, M, R = map(int, input().split())
N_MAX = 100000
M_MAX = 100000
graph_dfs = [[] for _ in range(N + 1)]
visited = [False] * N_MAX
answer = [0] * M_MAX
order = 1

for _ in range(M):
    x, y = map(int, input().split())
    graph_dfs[x].append(y)
    graph_dfs[y].append(x)


for i in range(1, N + 1):
    graph_dfs[i] = sorted(graph_dfs[i], reverse=True)

dfs(R)

for i in range(1, N + 1):
    print(answer[i])