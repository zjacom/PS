N = int(input())

arr = list(map(int, input().split()))

def recur(num, path):
    if len(path) > len(arr):
        return
    
    elif len(path) == len(arr):
        if sorted(path) == sorted(arr):
            print(path)
            exit(0)
        else:
            return
        
    if num % 3 == 0 and num // 3 in arr:
        recur(num // 3, path + [num // 3])
    if num * 2 in arr:
        recur(num * 2, path + [num * 2])

for num in arr:
    recur(num, [num])