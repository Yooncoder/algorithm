tc = 10
for t in range(1, tc + 1):
    n = int(input())
    board = [' '.join(list(map(str, input().split()))) for _ in range(100)]
    zboard = list(zip(*board))
    max_l = 0
    for m in range(1, 101):
        for i in range(100):
            for j in range(100 - m + 1):
                if board[i][j : j + m] == board[i][j : j + m][::-1]:
                    if max_l < len(board[i][j : j + m]):
                        max_l = len(board[i][j : j + m])
                if zboard[i][j : j + m] == zboard[i][j : j + m][::-1]:
                    if max_l < len(board[i][j : j + m]):
                        max_l = len(board[i][j : j + m])
    print('#{} {}'.format(t, max_l))