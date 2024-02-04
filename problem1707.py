import sys
input = sys.stdin.readline
from collections import defaultdict, deque

# input
K = int(input())

result = ["YES"] * K

def bfs(node):
    global visited, color

    q = deque([(node)])

    while q:
        cn = q.popleft()
        for nxt in graph[cn]:
            if not visited[nxt]:
                q.append(nxt)
                if color[cn] == 1:
                    color[nxt] == -1
                else:
                    color[nxt] == 1
            if color[cn] == color[nxt]:
                return False
    return True
                


for idx in range(K):
    V, E = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    # logic
    visited = [False] * (V + 1)
    visited[1] = True
    color = [0] * (V + 1)
    color[1] = 1
    if not bfs(1):
        result[idx] = "NO"
    
for r in result:
    print(r)