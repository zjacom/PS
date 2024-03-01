V, E = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(E)]
graph.sort(key=lambda x : x[2])

parent = [i for i in range(V + 1)]

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

answer = 0
for a, b, w in graph:
    a = find(a)
    b = find(b)

    if a == b:
        continue
    else:
        union(a, b)
        answer += w

print(answer)