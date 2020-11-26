dt = ((0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1))
for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    board = [[0] * n for _ in range(n)]
    mid = n // 2
    board[mid][mid] = board[mid - 1][mid - 1] = 2
    board[mid][mid - 1] = board[mid - 1][mid] = 1

    for i in range(m):
        x, y, c = map(int, input().split())
        x, y = y - 1, x - 1
        change = []
        for d in range(8):
            dx, dy = dt[d]
            nx, ny = x + dx, y + dy
            while True:
                if nx < 0 or ny < 0 or nx > n - 1 or ny > n - 1:
                    change = []
                    break
                if board[nx][ny] == 0:
                    change = []
                    break
                if board[nx][ny] == c:
                    break
                else:
                    change.append((nx, ny))
                nx, ny = nx + dx, ny + dy
            for i, j in change:
                if c == 1:
                    board[i][j] = 1
                else:
                    board[i][j] = 2
        board[x][y] = c
    w, b = 0, 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                b += 1
            elif board[i][j] == 2:
                w += 1
    print('#{} {} {}'.format(t, b, w))