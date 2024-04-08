from itertools import permutations

A, B = map(int, input().split())

arr = list(str(A))

maxi = -1

for a in list(permutations(arr, len(arr))):
    if a[0] != "0" and int(''.join(a)) < B:
        maxi = max(maxi, int(''.join(a)))

print(maxi)