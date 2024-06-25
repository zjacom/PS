# 1515번
import sys

s = list(input())

for num in range(1, sys.maxsize):
    if not s:
        print(num - 1)
        break
    temp = list(str(num))
    for n in temp:
        if s and s[0] == n:
            s.pop(0)
