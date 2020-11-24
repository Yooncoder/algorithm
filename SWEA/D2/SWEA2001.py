for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(n)]

    max_cnt = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            cnt = 0
            for r in range(i, i + m):
                for c in range(j, j + m):
                    cnt += fly[r][c]
            max_cnt = max(max_cnt, cnt)
    print('#{} {}'.format(t, max_cnt))