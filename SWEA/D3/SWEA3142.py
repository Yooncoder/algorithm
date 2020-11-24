tc = int(input())
for t in range(1, tc + 1):
    n, m = map(int, input().split())
    x = n - m
    y = m - x
    print('#{} {} {}'.format(t, y, x))