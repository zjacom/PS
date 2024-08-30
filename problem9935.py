s = input()
explosion = input()

stack, l = [], len(explosion)

for i in s:
    stack.append(i)
    if len(stack) >= l and ''.join(stack[-l:]) == explosion:
        for _ in range(l):
            stack.pop()


if not stack:
    print("FRULA")
else:
    print(''.join(stack))