from collections import defaultdict

s = input()

dic = defaultdict(int)
for i in s:
    dic[i.upper()] += 1

dic2 = defaultdict(list)
for key, value in dic.items():
    dic2[value].append(key)

maxi = max(dic2)

if len(dic2[maxi]) > 1:
    print('?')
else:
    print(dic2[maxi].pop())