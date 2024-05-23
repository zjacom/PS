N = int(input())

if N == 1:
    print(1)
    exit(0)
elif N <= 7:
    print(2)
    exit(0)

left, right = 2, 7
a, b = 1, 2
result = 3
while True:
    if left + (6 * a) <= N <= right + (6 * b):
        print(result)
        break

    left += (6 * a)
    right += (6 * b)
    a += 1
    b += 1
    result += 1