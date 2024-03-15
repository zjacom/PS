from collections import defaultdict, deque

N = int(input())

graph = defaultdict(list)

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

order = list(map(int, input().split()))
visited = [False] * (N + 1)
visited[1] = True
children = [set() for _ in range(N+1)] 
q = deque([1])

while q:
    node = q.popleft()
    for nxt in graph[node]:
        if not visited[nxt]:
            children[node].add(nxt)
            q.append(nxt)
            visited[nxt] = True
print(children)

next_index = 1
for i in order:
    if next_index == N:
        break
    c_length = len(children[i]) #자식의 길이
    c1 = set(order[next_index : next_index+c_length])
    c2 = children[i]
    if c1 != c2:
        print(0)
        exit()
    next_index += c_length

print(1)