from collections import defaultdict

p, m = map(int, input().split())

dic = defaultdict(list)

for _ in range(p):
    level, name = input().split()
    level = int(level)

    flag = False
    for key, value in dic.items():
        if value[0][0] - 10 <= level and level <= value[0][0] + 10 and len(value) < m:
            value.append((level, name))
            flag = True
            break
    
    if not flag:
        dic[name].append((level, name))

for _, value in dic.items():
    if len(value) == m:
        print("Started!")
        for level, name in sorted(value, key=lambda x: x[1]):
            print(level, name)
    else:
        print("Waiting!")
        for level, name in sorted(value, key=lambda x: x[1]):
            print(level, name)