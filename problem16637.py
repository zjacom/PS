import sys

N = int(input())
me = input()
orders = []
for m in me:
    if m.isdigit():
        orders.append(int(m))
    else:
        orders.append(m)
answer = -sys.maxsize


def operator(prev, s, nxt):
    if s == "*":
        return prev * nxt
    elif s == "+":
        return prev + nxt
    else:
        return prev - nxt


def calculator(arr):
    prev = arr[0]
    for i in range(1, len(arr) - 1, 2):
        prev = operator(prev, arr[i], arr[i + 1])
    return prev


def recur(idx, orders):
    global answer
    if idx >= len(orders):
        answer = max(answer, calculator(orders))
        return
    recur(idx + 2, orders)
    recur(idx + 2, orders[:idx-1] + [operator(orders[idx-1], orders[idx], orders[idx+1])] + orders[idx+2:])


recur(1, orders)
print(answer)