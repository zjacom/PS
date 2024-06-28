from itertools import permutations
from collections import defaultdict
N = int(input())

arr = list(map(int, input().split()))
able = list(permutations([n for n in range(1, N + 1)], N))
dic = defaultdict(int)
for i in range(N):
    dic[i + 1] = arr[i]

for arr in able:
    flag = True
    for i in range(N):
        num = arr[i]
        cnt = 0
        for j in range(i):
            if arr[j] > num:
                cnt += 1
        if dic[num] != cnt:
            flag = False
            break
    if flag:
        print(*arr)
        break
