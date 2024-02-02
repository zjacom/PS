import sys
input = sys.stdin.readline

# input
A, B = map(int, input().split())

# logic
def solution(num):
    result = num
    for i in range(1, 51):
        result += (num // (2 ** i)) * (2 ** (i - 1))
    return result

# output
print(solution(B) - solution(A - 1))