N = int(input())
arr = list(map(int, input().split()))

answer = 0

def recur(arr, total):
    global answer
    if len(arr) == 2:
        answer = max(answer, total)
        return
    
    for idx in range(1, len(arr) - 1):
        recur(arr[:idx] + arr[idx+1:], total + (arr[idx - 1] * arr[idx + 1]))

recur(arr, 0)
print(answer)