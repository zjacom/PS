# 1005번
from collections import defaultdict, deque

results = []
TC = int(input())
for _ in range(TC):
    N, K = map(int, input().split())
    costs = [0] + list(map(int, input().split()))
    dic = defaultdict(list)
    indegrees = [0] * (N + 1)
    for _ in range(K):
        a, b = map(int, input().split())
        dic[a].append(b)
        indegrees[b] += 1
    target = int(input())
    
    dp = [0] * (N + 1)
    q = deque()
    for i in range(1, N + 1):
        if not indegrees[i]:
            q.append(i)
            dp[i] = costs[i]
    
    while q:
        node = q.popleft()

        for nxt in dic[node]:
            indegrees[nxt] -= 1
            dp[nxt] = max(dp[nxt], dp[node] + costs[nxt])
            if not indegrees[nxt]:
                q.append(nxt)

    results.append(dp[target])


for res in results:
    print(res)