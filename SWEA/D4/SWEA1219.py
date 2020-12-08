def dfs(v):
    s = []
    s.append(v)
    visit[v] = True

    while len(s) > 0:
        if v == 99:
            return 1
        for w in g[v]:
            if not visit[w]:
                s.append(v)
                v = w
                visit[w] = True
                break
        else:
            v = s.pop()
    if v != 99:
        return 0


for i in range(10):
    v, e = map(int, input().split())
    case = list(map(int, input().split()))
    if e < 100:
        g = [[] for _ in range(100)]
        visit = [False for _ in range(100)]
    if e > 100:
        g = [[] for _ in range(e)]
        visit = [False for _ in range(e)]

    for j in range(0, len(case), 2):
        g[case[j]].append(case[j + 1])
    print('#{} {}'.format(i + 1, dfs(0)))