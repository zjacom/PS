from collections import Counter
import sys

T = int(input())

case = []
for _ in range(T):
    s = input()
    k = int(input())
    case.append((s, k))

for s, k in case:
    mini, maxi = sys.maxsize, -sys.maxsize
    
    print(maxi, mini)