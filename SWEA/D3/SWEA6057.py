def dfs(end, vertex, depth):
    global cnt
    if depth == 3:
        if end == vertex:
            cnt += 1
    else:
        for i in range(n):
            if visit[i] == 0 and lst[vertex][i] == 1:
                visit[i] = 1
                dfs(end, i, depth + 1)
                visit[i] = 0


for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(m)]
    lst = [[0] * n for _ in range(n)]
    visit = [0] * n
    cnt = 0

    for i in range(m):
        lst[data[i][0] - 1][data[i][1] - 1] = 1
        lst[data[i][1] - 1][data[i][0] - 1] = 1

    for i in range(n):
        for j in range(n):
            if j < i:
                visit[j] = 1
            else:
                visit[j] = 0
        for j in range(n):
            if lst[i][j] == 1 and visit[j] == 0:
                visit[j] = 1
                dfs(i, j, 1)

    print('#{} {}'.format(t, cnt))