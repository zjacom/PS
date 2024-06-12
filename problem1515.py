import sys

num = input()

arr = list(''.join(num))

number = 1
while arr:
    temp = list(''.join(str(number)))
    flag = False
    while temp and arr and temp[0] == arr[0]:
        flag = True
        temp.pop(0)
        arr.pop(0)
    if not flag:
        if arr[0] in str(number):
            arr.pop(0)
    number += 1

print(number - 1)