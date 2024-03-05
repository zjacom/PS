from itertools import combinations

N, S = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0

for num in arr:
    if num == S:
        answer += 1


for i in range(2, len(arr) + 1):
    for a in list(combinations(arr, i)):
        if sum(a) == S:
            answer += 1

print(answer)