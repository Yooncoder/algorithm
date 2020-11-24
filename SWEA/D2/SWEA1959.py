for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if n > m:
        n, m = m, n
        a, b = b, a
    max_v = float('-inf')
    for i in range(m - n + 1):
        sol = 0
        for j in range(n):
            sol += a[j] * b[i + j]
        max_v = max(max_v, sol)
    print('#{} {}'.format(t, max_v))