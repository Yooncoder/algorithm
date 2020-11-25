for t in range(1, int(input()) + 1):
    a, b, c = map(int, input().split())
    if a == b:
        print('#{} {}'.format(t, c))
    elif a == c:
        print('#{} {}'.format(t, b))
    elif b == c:
        print('#{} {}'.format(t, a))