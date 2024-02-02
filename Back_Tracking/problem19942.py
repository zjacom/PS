import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# input
N = int(input())
mp, mf, ms, mv = map(int, input().split())
ingre = [list(map(int, input().split())) for _ in range(N)]
result = []

# logic
def recur(idx, p, f, s, v, cost, path):
    if p >= mp and f >= mf and s >= ms and v >= mv:
        if result and min(result, key=lambda x: x[0])[0] > cost:
            result.append((cost, path[:]))
        elif not result:
            result.append((cost, path[:]))
    if idx == N:
        return
    recur(idx + 1, p + ingre[idx][0], f + ingre[idx][1], s + ingre[idx][2], v + ingre[idx][3], cost + ingre[idx][4], path + [idx])
    recur(idx + 1, p, f, s, v, cost, path)

# output
recur(0, 0, 0, 0, 0, 0, [])
if not result:
    print(-1)
else:
    cost, idx = min(result, key=lambda x: x[0])
    print(cost)
    for i in range(len(idx)):
        idx[i] += 1
    print(' '.join(map(str, idx)))
    