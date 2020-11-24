tc = int(input())

for i in range(1, tc + 1):
    water = list(map(int, input().split()))
    p = water[0]
    q = water[1]
    r = water[2]
    s = water[3]
    w = water[4]
    if w > r:
        if p * w < q + (s * (w - r)):
            print('#{} {}'.format(i, p * w))
        elif p * w > q + (s * (w - r)):
            print('#{} {}'.format(i, q + (s * (w - r))))
    if w < r:
        if p * w < q:
            print('#{} {}'.format(i, p * w))
        elif p * w > q:
            print('#{} {}'.format(i, q))