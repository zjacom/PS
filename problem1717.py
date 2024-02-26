import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# input
n, m = map(int, input().split())
# logic
parents = [i for i in range(n + 1)]


def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

result = []
for _ in range(m):
    t, a, b = map(int, input().split())
    if t == 0:
        union_parent(a, b)
    else:
        if find_parent(a) == find_parent(b):
            result.append("YES")
        else:
            result.append("NO")

for r in result:
    print(r)