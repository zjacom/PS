import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [-1] * (N + 1)
visited[1] = 0

for _ in range(N - 1):
    src, dst, cost = map(int, input().split())
    graph[src].append((dst, cost))
    graph[dst].append((src, cost))

def dfs(node, cost):
    global graph, visited
    for next_node, next_cost in graph[node]:
        cur_cost = cost + next_cost
        if visited[next_node] == -1:
            visited[next_node] = cur_cost
            dfs(next_node, cur_cost)
    
    return

dfs(1, 0)
index, temp = 0, 0
for i in range(1, N + 1):
    if visited[i] > temp:
        temp = visited[i]
        index = i

visited = [-1] * (N + 1)
visited[index] = 0
dfs(index, 0)

print(max(visited))