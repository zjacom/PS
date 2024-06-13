num = input()

arr = list(''.join(num))

number = 1
temp = list(str(number))
while arr:
    for n in temp:
        if arr and n == arr[0]:
            arr.pop(0)
    number += 1
    temp = list(str(number))
print(number - 1)