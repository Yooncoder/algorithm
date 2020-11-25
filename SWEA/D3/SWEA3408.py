for t in range(1, int(input()) + 1):
    n = int(input())
    s1 = (1 + n) * n // 2
    s2 = n ** 2
    s3 = (2 * n + 2) * n // 2
    print('#{} {} {} {}'.format(t, s1, s2, s3))