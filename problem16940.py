from collections import defaultdict, deque
from itertools import permutations

N = int(input())

graph = defaultdict(list)

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
answer = []
right = list(map(int, input().split()))

def recur(queue):
    global answer
    if not queue:
        return
    answer += queue[:]
    if len(answer) == N and answer == right:
        print(1)
        exit(0)
    for node in queue:
        visited[node] = True
    
    for node in queue:
        order = list(permutations(graph[node], len(graph[node])))
        temp = []
        for arr in order:
            for ele in arr:
                if not visited[ele]:
                    temp.append(ele)
        recur(temp)
        answer -= temp[:]

recur([1])