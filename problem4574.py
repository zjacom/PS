from itertools import combinations
block = list(combinations([num for num in range(1, 10)], 2))
sudoku = [[0] * 9 for _ in range(9)]
# 입력 받기
input_data = int(input())

for _ in range(input_data):
    u, lu, v, lv = map(str, input().split())
    u, v = int(u), int(v)
    y1, x1 = ord(lu[0]) - ord('A'), int(lu[1]) - 1
    y2, x2 = ord(lv[0]) - ord('A'), int(lv[1]) - 1
    sudoku[y1][x1], sudoku[y2][x2] = u, v

points = list(map(str, input().split()))

for idx, point in enumerate(points):
    y, x = ord(point[0]) - ord('A'), int(point[1]) - 1
    sudoku[y][x] = idx + 1

dirY, dirX = [1, -1, 0, 0], [0, 0, 1, -1]

def row_checker(y, num):
    for i in range(9):
        if num == sudoku[y][i]:
            return True
    return False

def col_checker(x, num):
    for i in range(9):
        if num == sudoku[i][x]:
            return True
    return False

def box_checker(y, x, num):
    if 0 <= y < 3:
        if 0 <= x < 3:
            for ny in range(3):
                for nx in range(3):
                    if sudoku[ny][nx] == num:
                        return True
            return False
        elif 3 <= x < 6:
            for ny in range(3):
                for nx in range(3, 6):
                    if sudoku[ny][nx] == num:
                        return True
            return False
        else:
            for ny in range(3):
                for nx in range(6, 9):
                    if sudoku[ny][nx] == num:
                        return True
            return False
    if 3 <= y < 6:
        if 0 <= x < 3:
            for ny in range(3, 6):
                for nx in range(3):
                    if sudoku[ny][nx] == num:
                        return True
            return False
        elif 3 <= x < 6:
            for ny in range(3, 6):
                for nx in range(3, 6):
                    if sudoku[ny][nx] == num:
                        return True
            return False
        else:
            for ny in range(3, 6):
                for nx in range(6, 9):
                    if sudoku[ny][nx] == num:
                        return True
            return False
    if 6 <= y < 9:
        if 0 <= x < 3:
            for ny in range(6, 9):
                for nx in range(3):
                    if sudoku[ny][nx] == num:
                        return True
            return False
        elif 3 <= x < 6:
            for ny in range(6, 9):
                for nx in range(3, 6):
                    if sudoku[ny][nx] == num:
                        return True
            return False
        else:
            for ny in range(6, 9):
                for nx in range(6, 9):
                    if sudoku[ny][nx] == num:
                        return True
            return False

def func(idx):
    if idx == len(block):
        for row in sudoku:
            print(*row)
        exit(0)
    
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == 0:
                for i in range(4):
                    ny, nx = y + dirY[i], x + dirX[i]
                    if 0 <= ny < 9 and 0 <= nx < 9:
                        if sudoku[ny][nx] == 0:
                            if not row_checker(y, block[i][0]) and not col_checker(x, block[i][0]) and not box_checker(y, x, block[i][0]):
                                if not row_checker(ny, block[i][1]) and not col_checker(nx, block[i][1]) and not box_checker(ny, nx, block[i][1]):
                                    sudoku[y][x], sudoku[ny][nx] = block[i][0], block[i][1]
                                    func(idx + 1)
                                    sudoku[y][x], sudoku[ny][nx] = 0, 0

                            elif not row_checker(y, block[i][1]) and not col_checker(x, block[i][1]) and not box_checker(y, x, block[i][1]):
                                if not row_checker(ny, block[i][0]) and not col_checker(nx, block[i][0]) and not box_checker(ny, nx, block[i][0]):
                                    sudoku[y][x], sudoku[ny][nx] = block[i][1], block[i][0]
                                    func(idx + 1)
                                    sudoku[y][x], sudoku[ny][nx] = 0, 0
func(0)