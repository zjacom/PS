left = list(input())
M = int(input())
right = []

for _ in range(M):
    commands = input()
    if commands[0] == "L" and left:
        right.append(left.pop())
    elif commands[0] == "D" and right:
        left.append(right.pop())
    elif commands[0] == "B" and left:
        left.pop()
    elif commands[0] == "P":
        left.append(commands[2])

answer = left + right[::-1]
print(''.join(answer))