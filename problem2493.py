N = int(input())

tops = list(map(int, input().split()))
stack = []
answer = []

for i in range(N):
    while stack and stack[-1][1] < tops[i]:
        stack.pop()
    if stack:
        answer.append(stack[-1][0])
    else:
        answer.append(0)
    stack.append((i + 1, tops[i]))

print(*answer)