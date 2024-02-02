from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 입력 및 설정
N = int(input())
graph = defaultdict(list)
result = [0] * (N + 1)
visited = [False] * (N + 1)

for _ in range(N - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 로직
def dfs(node):
    global graph, result, visited
    visited[node] = True

    for next_node in graph[node]:
        if not visited[next_node]:
            result[next_node] = node
            dfs(next_node)

# 결과 출력
dfs(1)

for i in range(2, N + 1):
    print(result[i])