from collections import deque

F, S, G, U, D = map(int, input().split())
visited = [-1] * 1_000_001
q = deque([(S)])
visited[S] = 0

while q:
    node = q.popleft()

    if node == G:
        break

    if node + U <= F and visited[node + U] == -1:
        q.append(node + U)
        visited[node + U] = visited[node] + 1
    if node - D > 0 and visited[node - D] == -1:
        q.append(node - D)
        visited[node - D] = visited[node] + 1

print(visited[G]) if visited[G] != -1 else print("use the stairs")