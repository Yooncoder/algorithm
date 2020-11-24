tc = 10
for t in range(1, tc + 1):
    n = int(input())
    board = [list(input()) for _ in range(8)]
    zboard = list(zip(*board))
    cnt = 0
    for i in range(8):
        for j in range(8 - n + 1):
            if board[i][j:j + n] == board[i][j:j + n][::-1]:
                cnt += 1
            if zboard[i][j:j + n] == zboard[i][j:j + n][::-1]:
                cnt += 1
    print('#{} {}'.format(t, cnt))