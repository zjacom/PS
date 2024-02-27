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
M = int(input())
cities = [city for city in range(N + 1)]
for idx in range(N):
    arr = list(map(int, input().split()))
    for jdx, value in enumerate(arr):
        if value == 1:
            union_city(idx + 1, jdx + 1)

root = list(map(int, input().split()))
result = "YES"
for idx in range(1, len(root)):
    if find(root[idx]) != find(root[idx - 1]):
        result = "NO"
        break

print(result)