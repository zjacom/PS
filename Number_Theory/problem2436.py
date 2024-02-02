import sys
input = sys.stdin.readline

A, B = map(int, input().split())

# logic & output
C = B // A


def GCD(a, b):
    while a % b != 0:
        a, b = b, a % b

    return b


for i in range(int(C ** 0.5), 0, -1):
    if C % i == 0 and GCD(i, C // i) == 1:
        print(i * A, C // i * A)
        break
