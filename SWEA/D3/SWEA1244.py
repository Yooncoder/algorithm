def dfs(n, cnt):
    global sol
    if cnt == 0:
        sol = max(sol, int(n))
        return
    if visit[cnt] > int(n):
        return
    visit[cnt] = int(n)

    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            n = list(n)
            n[i], n[j] = n[j], n[i]
            n = ''.join(n)
            dfs(n, cnt - 1)
            n = list(n)
            n[i], n[j] = n[j], n[i]
            n = ''.join(n)

for t in range(1, int(input()) + 1):
    n, cnt = map(str, input().split())
    cnt = int(cnt)
    sol = 0
    visit = [0] * 11
    dfs(n, cnt)
    print('#{} {}'.format(t, sol))