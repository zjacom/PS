N = int(input())

buildings = list(map(int, input().split()))

m = [0] * N

for i, h in enumerate(buildings):
    for j in range(i - 1, -1, -1):
        if buildings[j] > h:
            if abs(i - j) == 1:
                m[i] += 1
            break
        else:
            lean = (h - buildings[j]) / (i - j)
            flag = True
            for k in range(j + 1, i):
                if lean >= (h - buildings[k]) / (i - k):
                    flag = False
                    break
            if flag:
                m[i] += 1
    
    for j in range(i + 1, N):
        if buildings[j] > h:
            if abs(i - j) == 1:
                m[i] += 1
            break
        else:
            lean = (h - buildings[j]) / (i - j)
            flag = True
            for k in range(i + 1, j):
                if lean <= (h - buildings[k]) / (i - k):
                    flag = False
                    break
            if flag:
                m[i] += 1

print(max(m))