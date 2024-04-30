# 16637번
import sys

N = int(input())
me = list(input())
answer = -sys.maxsize


def calculator(prev, operator, next):
    if operator == "*":
        return prev * next
    elif operator == "+":
        return prev + next
    else:
        return prev - next
    

def make_result(arr):
    result = arr[0]
    for i in range(1, len(arr), 2):
        result = calculator(result, arr[i], arr[i + 1])
    return result


def recur(idx, arr):
    global answer
    
    if idx >= len(arr):
        answer = max(answer, make_result(arr))
        return
    
    recur(idx + 2, arr)
    recur(idx + 2, arr[:idx-1] + [calculator(arr[idx - 1], arr[idx], arr[idx + 1])] + arr[idx+2:])


for i in range(N):
    if me[i].isdigit():
        me[i] = int(me[i])

recur(1, me)
print(answer)