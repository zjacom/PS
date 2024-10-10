def solution(data, col, row_begin, row_end):
    data = sorted(data, key=lambda x: (x[col - 1], -x[0]))
    answer = 0
    tup = data[row_begin - 1]
    for e in tup:
        answer += (e % row_begin)
    for i in range(row_begin + 1, row_end + 1):
        tuple1 = data[i - 1]
        
        sum1 = 0
        for e in tuple1:
            sum1 += (e % i)
        answer = answer ^ sum1
    return answer