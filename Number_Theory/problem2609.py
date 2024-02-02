import sys
input = sys.stdin.readline

# input
A, B = map(int, input().split())

# logic
def GCD(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b

def LCM(a, b):
    return A * B // GCD(a, b)

# output
print(GCD(A, B))
print(LCM(A, B))