from itertools import combinations

N, L, R, X = map(int, input().split())

arr = list(map(int, input().split()))

answer = 0

for i in range(2, N + 1):
    for a in list(combinations(arr, i)):
        total = sum(a)
        if total >= L and total <= R and (max(a) - min(a)) >= X:
            answer += 1

print(answer)