import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def find(x):
    if cities[x] != x:
        cities[x] = find(cities[x])
    return cities[x]


def union_city(a, b):
    a = find(a)
    b = find(b)
    if a < b :
        cities[b] = a
    else:
        cities[a] = b


N = int(input())
cities = [city for city in range(N)]
M = int(input())
for idx in range(M):
    arr = list(map(int, input().split()))
    for jdx, value in enumerate(arr):
        if value == 1:
            union_city(idx, jdx)

root = list(map(int, input().split()))
result = "YES"
for idx in range(1, len(root)):
    if find(root[idx] - 1) != find(root[idx - 1] - 1):
        result = "NO"
        break

print(result)