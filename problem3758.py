from collections import defaultdict

result = []
T = int(input())

for _ in range(T):
    n, k, t, m = map(int, input().split())
    scores = defaultdict(lambda: [0] * (k + 1))
    order = [0] * (n + 1)
    count = defaultdict(int)

    for idx in range(m):
        i, j, s = map(int, input().split())
        order[i] = idx
        scores[i][j] = max(scores[i][j], s)
        count[i] += 1
    
    teams = [n for n in range(1, n + 1)]
    teams.sort(key=lambda x: (sum(scores[x]), -count[x], -order[x]), reverse=True)
    result.append(teams.index(t) + 1)


for res in result:
    print(res)