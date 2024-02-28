import sys
input = sys.stdin.readline
from collections import Counter

G = int(input())
P = int(input())
gates = [-1] * G
gi = []
for _ in range(P):
    gi.append(int(input()))
print(gi)

for cnt in range(len(gi)):
    print(gates)
    counter = Counter(gates)
    flag = False
    for idx in range(gi[cnt]):
        if gates[idx] == -1:
            gates[idx] = cnt + 1
            flag = True
        else:
            if counter[cnt + 1] > 1:
                gates[idx] = cnt + 1
                counter[cnt + 1] -= 1
                flag = True
    if not flag:
        print(cnt)
        break
