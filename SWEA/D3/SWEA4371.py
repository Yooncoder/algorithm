for t in range(1, int(input()) + 1):
    n = int(input())
    data = [int(input()) for _ in range(n)]
    sol = []
    res = []

    for i in range(1, n):
        sol.append(data[i] - 1)
    for i in range(len(sol) - 1):
        for j in range(i + 1, len(sol)):
            if sol[j] % sol[i] == 0:
                res.append(sol[j])
    for i in res:
        if i in sol:
            sol.remove(i)
    print('#{} {}'.format(t, len(sol)))