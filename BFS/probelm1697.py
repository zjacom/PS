from collections import deque
import sys
input = sys.stdin.readline

# 입력
N, K = map(int, input().split())

# 로직
q = deque([(N)])
MAX = 100000
visited = [0] * (MAX + 1)

while q:
    node = q.popleft()
    if node == K:
        print(visited[node])
        exit(0)
    for i in (node - 1, node + 1, node * 2):
        if 0 <= i <= MAX and not visited[i]:
            visited[i] = visited[node] + 1
            q.append(i)