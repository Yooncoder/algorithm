for t in range(1, int(input()) + 1):
    l, u, x = map(int, input().split())
    if l <= x <= u:
        print('#{} {}'.format(t, 0))
    elif x < l:
        print('#{} {}'.format(t, l - x))
    elif u < x:
        print('#{} {}'.format(t, -1))