for t in range(1, int(input()) + 1):
    n = int(input())
    crop = [list(map(int, input())) for _ in range(n)]
    val = 0
    for i in range(n // 2 + 1):
        for j in range(2 * i + 1):
            val += crop[i][n // 2 - i + j]
    for i in range(n // 2 + 1, n):
        for j in range(2 * (n - i - 1) + 1):
            val += crop[i][n // 2 + (i - n + 1) + j]
    print('#{} {}'.format(t, val))