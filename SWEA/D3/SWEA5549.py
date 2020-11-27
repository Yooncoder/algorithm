for t in range(1, int(input()) + 1):
    n = int(input())
    sol = n % 2
    if sol == 1:
        print('#{} {}'.format(t, 'Odd'))
    else:
        print('#{} {}'.format(t, 'Even'))