tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    ju = ''
    for i in range(n):
        ju += '1/' + str(n) + ' '
    print('#{} {}'.format(t, ju[:-1]))