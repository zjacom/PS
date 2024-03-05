from itertools import combinations

N = int(input())
S = list(map(int, input().split()))


arr = set()
for num in S:
    arr.add(num)

for i in range(2, len(S) + 1):
    for li in list(combinations(S, i)):
        arr.add(sum(li))

for num in range(1, 2_000_001):
    if num not in arr:
        print(num)
        break
