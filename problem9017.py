from collections import defaultdict, Counter
import sys

result = []

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    p = []
    counter = Counter(arr)
    for key, value in counter.items():
        if value == 6:
            p.append(key)

    dic = defaultdict(list)

    idx = 1
    for i in range(N):
        if arr[i] in p:
            dic[arr[i]].append(idx)
            idx += 1
            
    mini, answer, fifth = sys.maxsize, 0, 0
    for key, value in dic.items():
        if sum(value[:4]) < mini:
            mini = sum(value[:4])
            answer = key
            fifth = value[4]
        elif sum(value[:4]) == mini and value[4] < fifth:
            mini = sum(value[:4])
            answer = key
            fifth = value[4]
    result.append(answer)

for res in result:
    print(res)

