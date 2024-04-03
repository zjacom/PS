A, B, C, X, Y = map(int, input().split())

answer = 0

if A + B > 2 * C:
    while X > 0 and Y > 0:
        answer += 2 * C
        X -= 1
        Y -= 1

if A > 2 * C:
    while X > 0:
        answer += 2 * C
        X -= 1
else:
    while X > 0:
        answer += A
        X -= 1

if B > 2 * C:
    while Y > 0:
        answer += 2 * C
        Y -= 1
else:
    while Y > 0:
        answer += B
        Y -= 1

print(answer)