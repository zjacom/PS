sudoku = [list(map(int, input().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append([i,j])
    
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

def recur(idx):
    if idx == len(blank):
        for row in sudoku:
            print(*row)
        exit(0)
    
    for num in range(1, 10):
        y, x = blank[idx][0], blank[idx][1]
        if not row_checker(y, num) and not col_checker(x, num) and not box_checker(y, x, num):
            sudoku[y][x] = num
            recur(idx + 1)
            sudoku[y][x] = 0

recur(0)