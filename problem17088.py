import copy
import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
B = list(map(int, input().split()))
answer = sys.maxsize

if N < 3:
    print(0)
    exit()

def checker(a, b, x, y):
    cnt = abs(a) + abs(b)

    new_x, new_y = x + a, y + b

    return new_y - new_x, new_x, new_y, cnt


for i in range(-1, 2):
    for j in range(-1, 2):
        s, new_x, new_y, cnt = checker(i, j, B[0], B[1])
        
        temp = B[:]
        temp[0], temp[1] = new_x, new_y
        flag = True
        for k in range(2, len(temp)):
            if temp[k] - temp[k - 1] == s:
                continue
            elif temp[k] - 1 - temp[k - 1] == s:
                temp[k] -= 1
                cnt += 1
            elif temp[k] + 1 - temp[k - 1] == s:
                temp[k] += 1
                cnt += 1
            else:
                flag = False
                break
        if flag:
            answer = min(answer, cnt)

if answer == sys.maxsize:
    print(-1)
else:
    print(answer)
                
