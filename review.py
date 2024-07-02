# 1406번

s = list(input())
N = int(input())
stack = []
for _ in range(N):
    i = input()
    if i[0] == "P":
        s.append(i[2])
    elif i[0] == "L" and s:
        stack.append(s.pop())
    elif i[0] == "D" and stack:
        s.append(stack.pop())
    elif i[0] == "B" and s:
        s.pop()

print(''.join(s + stack[::-1]))
