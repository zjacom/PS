from collections import deque, defaultdict

N = int(input())
first_line = [n for n in range(1, N + 1)]
second_line = [int(input()) for _ in range(N)]
dic = defaultdict(list)
for i in range(N):
    dic[first_line[i]].append(second_line[i])

answer = set()
for i in range(N):
    if first_line[i] == second_line[i]:
        answer.add(first_line[i])

    else:
        q = deque([(first_line[i], [first_line[i]])])
        visited = [0] * (N + 1)
        visited[first_line[i]] = 1

        while q:
            node, path = q.popleft()
            if len(path) > 1 and path[-1] == first_line[i]:
                for num in path:
                    answer.add(num)
                break

            for nxt in dic[node]:
                if len(path) < N:
                    q.append((nxt, path + [nxt]))

print(len(answer))
answer = sorted(list(answer))
for n in answer:
    print(n)
