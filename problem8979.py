N, K = map(int, input().split())

orders = []

for _ in range(N):
    num, g, s, b = map(int, input().split())
    orders.append([num, g, s, b])

orders.sort(key= lambda x: (x[1], x[2], x[3]), reverse=True)

prev, prev_medal = 0, 0

dic = {}
for i, v in enumerate(orders):
    if prev_medal != v[1:]:
        dic[v[0]] = i + 1
        prev, prev_medal = i + 1, v[1:]
    else:
        dic[v[0]] = prev

print(dic[K])