tc = int(input())
for t in range(1, tc + 1):
    board = [[0] * 300 for _ in range(300)]
    cnt = 1
    for i in range(1, 300):
        x = i
        y = 1
        for j in range(1, i + 1):
            board[x][y] = cnt
            cnt += 1
            x -= 1
            y += 1
    p, q = map(int, input().split())
    p_point = (0, 0)
    q_point = (0, 0)
    for i in range(1, 300):
        for j in range(1, 300):
            if board[i][j] == p:
                p_point = (i, j)
            if board[i][j] == q:
                q_point = (i, j)
    new_point = (p_point[0] + q_point[0], p_point[1] + q_point[1])
    sol = board[new_point[0]][new_point[1]]
    print('#{} {}'.format(t, sol))