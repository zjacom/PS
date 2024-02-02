import collections

# 입력
N = int(input())
relations = []

for _ in range(N):
    relations.append(input())

# 세팅
graph = collections.defaultdict(list)

for index1, str in enumerate(relations):
    for index2, char in enumerate(str):
        if char == "Y":
            graph[index1 + 1].append(index2 + 1)

# 로직
def bfs(num, cnt):
    discovered = []
    queue = collections.deque([(num, cnt)])

    while queue:
        node, count = queue.popleft()
        if node not in discovered:
            discovered.append(node)

            if count >= 1:
                for x in graph[node]:
                    queue.append((x, count - 1))
    
    return len(discovered) - 1

result = 0

for key in list(graph):
    result = max(result, bfs(key, 2))

print(result)