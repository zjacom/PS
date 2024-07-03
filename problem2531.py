from collections import deque

N, d, k, c = map(int, input().split())

sushi = [int(input()) for _ in range(N)]

cases = deque()

left, right = 0, k - 1

for i in range(k):
    cases.append(sushi[i])

answer = -1
while left < N:
    if c in cases:
        answer = max(answer, len(set(cases)))
    else:
        answer = max(answer, len(set(cases)) + 1)
    
    left += 1
    cases.popleft()
    right += 1
    cases.append(sushi[right % N])

print(answer)