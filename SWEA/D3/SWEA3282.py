def knapsack(k, v, c, n):
    data = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(k + 1):
            if i == 0 or j == 0:
                data[i][j] = 0
            elif v[i - 1] <= j:
                data[i][j] = max(c[i - 1] + data[i - 1][j - v[i - 1]], data[i - 1][j])
            else:
                data[i][j] = data[i - 1][j]
    return data[n][k]


tc = int(input())
for t in range(1, tc + 1):
    n, k = map(int, input().split())
    v = []
    c = []
    for i in range(n):
        x, y = map(int, input().split())
        v.append(x)
        c.append(y)
    print('#{} {}'.format(t, knapsack(k, v, c, n)))