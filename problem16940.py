from collections import defaultdict, deque

N = int(input())

graph = defaultdict(list)

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
visited[1] = True
answer, path = deque([1]), []
right = list(map(int, input().split()))


def recur():
    global answer, path, visited
    print(answer, path)
    while answer:
        node = answer.pop()
        path.append(node)
        temp = []
        for nxt in graph[node]:
            if not visited[nxt]:
                temp.append(nxt)
                visited[nxt] = True
        if temp:
            count = len(temp)
            print(count)
            for idx in range(len(temp)):
                answer += temp[idx:] + temp[:idx]
                recur()
                for _ in range(count):
                    visited[answer.pop()] = False
                    path.pop()

recur()