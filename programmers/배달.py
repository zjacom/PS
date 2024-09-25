from collections import defaultdict, deque
import sys


def checking(N, graph, dest):
    result = sys.maxsize
    visited = [-1] * (N + 1)
    visited[1] = 0
    q = deque([1])
    while q:
        node = q.popleft()
        if node == dest:
            result = min(result, visited[dest])
            continue
        for nxt, cost in graph[node]:
            if visited[nxt] == -1 or visited[nxt] > visited[node] + cost:
                q.append(nxt)
                visited[nxt] = visited[node] + cost
    return result


def solution(N, road, K):
    answer = 0
    graph = defaultdict(list)
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    for node in range(1, N + 1):
        cost = checking(N, graph, node)
        if cost <= K:
            answer += 1
    return answer
