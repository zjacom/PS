import sys
input = sys.stdin.readline

# input
N = int(input())
result = [0]
w = []
x_list, y_list = set(), set()
for _ in range(N):
    x, y = map(int, input().split())
    x_list.add(x)
    y_list.add(y)
    w.append((x, y))

# logic
# 2차원 배열에서 만나는 지점이 될 수 있는 모든 경우의 수
able_list = []
for x in x_list:
    for y in y_list:
        able_list.append((x, y))

# 입력 받은 모든 수와 위에서 구한 모든 지점의 차이를 모두 계산하고 정렬
total_distance_list = []
for point in able_list:
    temp = []
    for i in range(N):
        temp.append(abs(point[0] - w[i][0]) + abs(point[1] - w[i][1]))
    total_distance_list.append(sorted(temp))

result = [0]
for i in range(2, N + 1):
    cnt = sys.maxsize
    for d in total_distance_list:
        cnt = min(cnt, sum(d[:i]))
    result.append(cnt)

# output
print(' '.join(map(str, result)))
