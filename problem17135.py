from itertools import combinations

N, M, D = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
archers = list(combinations([i for i in range(M)], 3))
enemies = []

for y in range(N):
    for x in range(M):
        if graph[y][x] == 1:
            enemies.append((y, x))

def custom_sort(point, x, y):
    a, b = point[0], point[1]
    return (abs(x - a) + abs(y - b), b)


def attack(a1, a2, a3, enemy):
    count = 0
    while enemy:
        killed_by_a1 = sorted(enemy, key=lambda e: custom_sort(e, a1[0], a1[1]))[0]
        killed_by_a2 = sorted(enemy, key=lambda e: custom_sort(e, a2[0], a2[1]))[0]
        killed_by_a3 = sorted(enemy, key=lambda e: custom_sort(e, a3[0], a3[1]))[0]

        if abs(a1[0]- killed_by_a1[0]) + abs(a1[1] - killed_by_a1[1]) <= D:
            enemy.remove(killed_by_a1)
            count += 1
        if abs(a2[0]- killed_by_a2[0]) + abs(a2[1] - killed_by_a2[1]) <= D:
            if killed_by_a2 in enemy:
                enemy.remove(killed_by_a2)
                count += 1
        if abs(a3[0]- killed_by_a3[0]) + abs(a3[1] - killed_by_a3[1]) <= D:
            if  killed_by_a3 in enemy:
                enemy.remove(killed_by_a3)
                count += 1
        
        temp = []
        for i in range(len(enemy)):
            if enemy[i][0] + 1 == N:
                continue
            else:
                temp.append((enemy[i][0] + 1, enemy[i][1]))
        
        enemy = temp
    
    return count

result = -10000
for archer in archers:
    result = max(result, attack((N, archer[0]), (N, archer[1]), (N, archer[2]), enemies[:]))

print(result)