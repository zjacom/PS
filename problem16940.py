from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N = int(input())

graph = defaultdict(list)

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

right = list(map(int, input().split()))
q = deque([1])
visited = [-1] * (N + 1)
visited[1] = 0
childrens = [{1}]

while q:
    node = q.popleft()
    temp = set()
    for nxt in graph[node]:
        if visited[nxt] == -1:
            q.append(nxt)
            visited[nxt] = node
            temp.add(nxt)
    if temp:
        childrens.append(temp)

answer = 1
start = 0
for children in childrens:
    length = len(children)
    if children != set(right[start:start+length]):
        answer = 0
        break
    start = start + length
print(answer)