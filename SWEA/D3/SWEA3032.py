def eucl(x, y):
    if x < y:
        r1, r2 = y, x
    r1, r2 = x, y
    s1, s2 = 1, 0
    t1, t2 = 0, 1

    while r2 > 0:
        q = r1 // r2
        r = r1 - q * r2
        r1, r2 = r2, r

        s = s1 - q * s2
        s1, s2 = s2, s

        t = t1 - q * t2
        t1, t2 = t2, t
    return s1, t1

tc = int(input())
for t in range(1, tc + 1):
    a, b = map(int, input().split())

    print('#{} {} {}'.format(t, eucl(a, b)[0], eucl(a, b)[1]))