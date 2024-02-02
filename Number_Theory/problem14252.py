import sys
input = sys.stdin.readline

# input
N = int(input())
arr = sorted(list(map(int, input().split())))

# logic
def GCD(a, b):
    while a % b != 0 :
        a, b = b, a % b

    return b

def insert(x, y):
    for num in range(x + 1, y):
        if GCD(num, y) == 1 and GCD(x, num) == 1:
            return 1
    return 2

result = 0
for i in range(len(arr) - 1):
    if GCD(arr[i], arr[i + 1]) != 1:
        result += insert(arr[i], arr[i + 1])

print(result)