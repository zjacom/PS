from collections import defaultdict
from itertools import combinations
import sys

N, M = map(int, input().split())

dic = defaultdict(list)
answer = sys.maxsize

for _ in range(M):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

for i in range(1, N + 1):
    if len(dic[i]) >= 2:
        cases = list(combinations(dic[i], 2))
        # i, case[0], case[1]
        for case in cases:
            if case[1] in dic[case[0]]:
                answer = min(answer, len(dic[i]) + len(dic[case[0]]) + len(dic[case[1]]) - 6)

if answer == sys.maxsize:
    print(-1)
else:
    print(answer)