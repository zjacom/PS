from collections import defaultdict, deque

TC = int(input())
results = []

for _ in range(TC):
    N, K = map(int, input().split())
    costs = list(map(int, input().split()))
    graph = defaultdict(list)
    indegrees = [0] * (N + 1)
    dp = [-1] * (N + 1)
    for _ in range(K):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegrees[b] += 1
    W = int(input())

    q = deque()
    for i in range(1, N + 1):
        if indegrees[i] == 0:
            q.append(i)
            dp[i] = costs[i - 1]

    while q:
        node = q.popleft()
        for nxt in graph[node]:
            indegrees[nxt] -= 1
            dp[nxt] = max(dp[nxt], dp[node] + costs[nxt - 1])
            if indegrees[nxt] == 0:
                q.append(nxt)

    results.append(dp[W])

for res in results:
    print(res)