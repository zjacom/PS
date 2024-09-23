from collections import defaultdict
from itertools import combinations


def solution(orders, course):
    dic = defaultdict(int)
    p = defaultdict(int)
    for order in orders:
        order = sorted(order)
        for c in course:
            cases = list(combinations(order, c))
            if cases:
                for case in cases:
                    s = "".join(case)
                    dic[s] += 1
                    p[c] = max(p[c], dic[s])
    result = []
    print(dic)
    for key, value in dic.items():
        for length, count in p.items():
            if len(key) == length and value == count and value > 1:
                result.append(key)
                break
    return sorted(result)
