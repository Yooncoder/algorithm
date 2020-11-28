for t in range(1, int(input()) + 1):
    n = int(input())
    sol = 0
    for i in range(n):
        p, x = map(float, input().split())
        sol += p * x
    print('#{0} {1:.6f}'.format(t, sol))