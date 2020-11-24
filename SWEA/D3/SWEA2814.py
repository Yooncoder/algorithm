def route(s):
    global cnt, max_cnt
    visit[s] = 1
    cnt += 1
    if cnt > max_cnt:
        max_cnt = cnt
    for i in range(1, n + 1):
        if not visit[i] and g[s][i]:
            route(i)
            visit[i] = 0
            cnt -= 1

tc = int(input())
for t in range(1, tc + 1):
    n, m = map(int, input().split())
    g = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(m):
        x, y = map(int, input().split())
        g[x][y] = 1
        g[y][x] = 1
    max_cnt = 0

    for i in range(1, n + 1):
        visit = [0] * (n + 1)
        cnt = 0
        route(i)
    print('#{} {}'.format(t, max_cnt))