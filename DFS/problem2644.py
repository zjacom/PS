from collections import defaultdict 

# 입력
n = int(input())
src, dst = map(int, input().split())
m = int(input())

# 설정
graph = defaultdict(list)
discovered = []
answer = -1

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 로직
def dfs(node, count):
    global graph, discovered, dst, answer

    if node == dst:
        answer = count
        return
    
    if node not in discovered:
        discovered.append(node)
        for next_node in graph[node]:
            dfs(next_node, count + 1)

# 결과 출력
dfs(src, 0)
print(answer)
