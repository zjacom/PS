def solution(rows, columns, queries):
    answer = []
    graph = [[x for x in range((columns * y) + 1, (columns * (y + 1)) + 1)] for y in range(rows)]
    for y1, x1, y2, x2 in queries:
        arr = []
        x1, x2, y1, y2 = min(x1, x2) - 1, max(x1, x2) - 1, min(y1, y2) - 1, max(y1, y2) - 1
        for x in range(x1, x2 + 1):
            arr.append(graph[y1][x])
        for y in range(y1 + 1, y2 + 1):
            arr.append(graph[y][x2])
        for x in range(x2 - 1, x1 - 1, -1):
            arr.append(graph[y2][x])
        for y in range(y2 - 1, y1, -1):
            arr.append(graph[y][x1])
        answer.append(min(arr))
        idx = 0
        for x in range(x1 + 1, x2 + 1):
            graph[y1][x] = arr[idx]
            idx += 1
        for y in range(y1 + 1, y2 + 1):
            graph[y][x2] = arr[idx]
            idx += 1
        for x in range(x2 - 1, x1 - 1, -1):
            graph[y2][x] = arr[idx]
            idx += 1
        for y in range(y2 - 1, y1 - 1, -1):
            graph[y][x1] = arr[idx]
            idx += 1
    return answer