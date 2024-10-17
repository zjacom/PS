def solution(n):
    answer = []
    
    def hanoi(src, dst, stop, num):
        if num == 1:
            answer.append([src, dst])
            return
        hanoi(src, stop, dst, num - 1)
        hanoi(src, dst, stop, 1)
        hanoi(stop, dst, src, num - 1)
    
    hanoi(1, 3, 2, n)
    return answer