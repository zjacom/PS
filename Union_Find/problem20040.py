import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union_parent(a, b):
    a, b = find(a), find(b)
    if a == b:
        return True
    elif a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [num for num in range(n)]
result = 0
arr = []
for idx in range(m):
    a, b = map(int, input().split())
    arr.append((a, b))

for idx, value in enumerate(arr):
    if union_parent(value[0], value[1]):
        result = idx + 1
        break

print(result)
