import heapq

def solution(n, k, enemy):
    answer = 0
    if len(enemy) <= k:
        return len(enemy)
    
    q = []
    
    for i in range(len(enemy)):
        heapq.heappush(q, enemy[i])
        if len(q) > k:
            node = heapq.heappop(q)
            if node > n:
                return i
            n -= node
    return len(enemy)