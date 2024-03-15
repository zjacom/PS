from collections import defaultdict

N = int(input())

graph = defaultdict(list)

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

order = list(map(int, input().split()))
childs = [[] for _ in range(N + 1)]

visited = [-1] * (N + 1)

def dfs(node, prev):
    visited[node] = prev

    for nxt in graph[node]:
        if visited[nxt] == -1:
            childs[node].append(nxt)
            dfs(nxt, node)

dfs(1, 0)
# 다음 노드가 자식이라면?
    # O -> idx + 1
    # X -> 첫 비교 노드의 자식 노드인지 확인하고
# 만약 해당 노드의 자식이 없는게 조회된다면 오류!
idx = 0
while idx < len(order):
    if order[idx + 1] in childs[idx]:
        idx += 1
    else:

print(childs)