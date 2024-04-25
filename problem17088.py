import copy
import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
B = list(map(int, input().split()))
answer = sys.maxsize


def checker(arr):
    if len(arr) <= 2:
        return True

    sub = arr[1] - arr[0]

    for i in range(2, len(arr)):
        if arr[i] - arr[i - 1] != sub:
            return False
    return True


q = [(0, B, 0)]

def recur(idx, arr, cnt):
    global answer

    if idx == N:
        if checker(arr):
            answer = min(answer, cnt)
        return
    
    # 0
    temp = copy.deepcopy(arr)
    recur(idx + 1, arr, cnt)
    arr = copy.deepcopy(temp)
    # 1
    temp = copy.deepcopy(arr)
    arr[idx] = arr[idx] + 1
    recur(idx + 1, arr, cnt + 1)
    arr = copy.deepcopy(temp)
    # -1
    temp = copy.deepcopy(arr)
    arr[idx] = arr[idx] - 1
    recur(idx + 1, arr, cnt + 1)
    arr = copy.deepcopy(temp)


recur(0, B, 0)
if answer == sys.maxsize:
    print(-1)
else:
    print(answer)