from collections import defaultdict

N = int(input())
T = int(input())

dic = defaultdict(list)
discovered = []

for _ in range(T):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)


def dfs(node):
    global dic, discovered
    discovered.append(node)

    for n in dic[node]:
        if n not in discovered:
            dfs(n)
    return


dfs(1)
print(len(discovered) - 1)
