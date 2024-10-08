import math

def solution(n, k):
    answer = []
    arr = [n for n in range(1, n + 1)]
    k -= 1
    
    while arr:
        fac = math.factorial(n - 1)
        idx = k // fac
        answer.append(arr.pop(idx))
        k = k % fac
        n -= 1
    return answer