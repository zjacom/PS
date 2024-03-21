from collections import deque

s, t = map(int, input().split())

if s == t:
    print(0)
    exit(0)

q = deque([(s, "")])
visited = [s]

while q:
    node, path = q.popleft()

    if node == t:
        print(path)
        exit(0)
    
    if node ** 2 < (10 ** 9 + 1) and (node ** 2) not in visited:
        q.append((node ** 2, path + "*"))
        visited.append(node ** 2)
    if node * 2 < (10 ** 9 + 1) and (node * 2) not in visited:
        q.append((node * 2, path + "+"))
        visited.append(node * 2)
    if 1 not in visited:
        q.append((1, path + "/"))
        visited.append(1)
print(-1)