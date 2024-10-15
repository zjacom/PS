def solution(board):
    answer = 0

    dp = [[0] * len(board[0]) for _ in range(len(board))]
    
    for y in range(len(board)):
        dp[y][0] = board[y][0]
        if board[y][0] == 1:
            answer = 1
    for x in range(len(board[0])):
        dp[0][x] = board[0][x]
        if board[0][x] == 1:
            answer = 1
    
    for y in range(1, len(board)):
        for x in range(1, len(board[0])):
            if board[y][x] == 1:
                dp[y][x] = min(dp[y - 1][x], dp[y][x - 1], dp[y - 1][x - 1]) + 1
                answer = max(answer, dp[y][x])
    
    return answer ** 2