stack = []
maxi = -1

def solution(n, info):
    recur(n, info, 0, [])
    if not stack:
        return [-1]
    return stack[0]

def recur(n, info, idx, path):
    global stack, maxi
    if len(info) == len(path):
        if n > 0:
            path[-1] += n
        raw, new = 0, 0
        for i in range(len(info)):
            if info[i] or path[i]:
                if info[i] >= path[i]:
                    raw += (10 - i)
                else:
                    new += (10 - i)
        if new > raw:
            if not stack:
                stack.append(path[:])
                maxi = max(maxi, new - raw)
                return
            if stack:
                if maxi < (new - raw):
                    while stack:
                        stack.pop()
                    stack.append(path[:])
                    maxi = max(maxi, new - raw)
                    return
                elif maxi == (new - raw):
                    node = stack[0]
                    a, b = 0, 0
                    for j in range(len(node)):
                        if node[j] > 0:
                            a = j
                        if path[j] > 0:
                            b = j
                    if a == b:
                        if node[j] < path[j]:
                            stack.pop()
                            stack.append(path[:])
                    elif a < b:
                        stack.pop()
                        stack.append(path[:])
        return
            
    if info[idx] < n:
        recur(n - info[idx] - 1, info, idx + 1, path + [info[idx] + 1])
    recur(n, info, idx + 1, path + [0])