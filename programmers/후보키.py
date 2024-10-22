from itertools import combinations

def solution(relation):
    pk = []
    for n in range(1, len(relation[0]) + 1):
        for cols in list(combinations([n for n in range(len(relation[0]))], n)):
            col = ''.join([str(i) for i in cols])
            flag = func(pk, col)
            if not flag:
                continue
            temp = set()
            for row in relation:
                data = ''.join([row[i] for i in cols])
                temp.add(data)
            if len(temp) == len(relation):
                pk.append(col)
    return len(pk)


def func(pk, col):
    # 최소성을 제대로 체크하기 위해 부분집합 관계 확인
    for key in pk:
        if set(key).issubset(set(col)):  # key가 col의 부분집합이면 최소성 위배
            return False
    return True