tc = int(input())

for t in range(1, tc + 1):
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    board_zip = list(zip(*board))
    cnt = 0
    word = 0
    for i in board:
        for j in i:
            if j:
                cnt += 1
            else:
                if cnt == k:
                    word += 1
                cnt = 0
        if cnt == k:
            word += 1
        cnt = 0
    for i in board_zip:
        for j in i:
            if j:
                cnt += 1
            else:
                if cnt == k:
                    word += 1
                cnt = 0
        if cnt == k:
            word += 1
        cnt = 0
    print('#{} {}'.format(t, word))