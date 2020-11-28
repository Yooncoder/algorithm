for t in range(1, int(input()) + 1):
    n = int(input())
    route = [0] * 5000
    for i in range(n):
        a, b = map(int, input().split())
        for j in range(a - 1, b):
            route[j] += 1

    p = int(input())

    sol = []
    for i in range(p):
        sol.append(route[int(input()) - 1])
    print('#{}'.format(t), *sol)