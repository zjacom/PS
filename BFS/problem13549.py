from collections import deque

N, K = map(int, input().split())

q = deque([N])
visited = [-1] * 100001
visited[N] = 0

while q:
    node = q.popleft()
    if node == K:
        print(visited[node])
        break
    if node - 1 >= 0 and visited[node - 1] == -1:
        q.append(node - 1)
        visited[node - 1] = visited[node] + 1
    if 2 * node <= 100000 and visited[2 * node] == -1:
        q.append(2 * node)
        visited[2 * node] = visited[node]
    if node + 1 <= 100000 and visited[node + 1] == -1:
        q.append(node + 1)
        visited[node + 1] = visited[node] + 1