# 19637번
N, M = map(int, input().split())

styles = []
for _ in range(N):
    a, b = input().split()
    styles.append((a, int(b)))

result = []

for _ in range(M):
    num = int(input())

    left, right = 0, len(styles) - 1

    while left <= right:
        mid = (left + right) // 2
        if styles[mid][1] >= num:
            right = mid - 1
        else:
            left = mid + 1
    result.append(styles[left][0])

for res in result:
    print(res)