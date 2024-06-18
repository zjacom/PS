T = int(input())
result = []
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr = arr[::-1]
    maxi, total = 0, 0
    for num in arr:
        if not maxi:
            maxi = num
        if maxi > num:
            total += (maxi - num)
        else:
            maxi = num
    result.append(total)

for res in result:
    print(res)
