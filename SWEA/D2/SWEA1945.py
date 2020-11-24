tc = int(input())

for i in range(1, tc + 1):
    num = int(input())
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    while num % 2 == 0:
        num = num // 2
        a += 1

    while num % 3 == 0:
        num = num // 3
        b += 1

    while num % 5 == 0:
        num = num // 5
        c += 1

    while num % 7 == 0:
        num = num // 7
        d += 1

    while num % 11 == 0:
        num = num // 11
        e += 1

    print('#{} {} {} {} {} {}'.format(i, a, b, c, d, e))