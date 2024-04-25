import copy

arr = [1, 2, 3, 4]
drr = arr[:]

def func(a):
    a[0] = 5
    return a

brr = func(arr)
# crr = func(copy.deepcopy(arr))
print(brr)
print(arr)
# print(crr)
print(drr)