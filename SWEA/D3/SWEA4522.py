for t in range(1, int(input()) + 1):
    st = input()
    res = True
    for i in range(len(st) // 2):
        if st[i] == '?':
            continue
        if st[len(st) - 1 - i] == '?':
            continue
        if st[i] != st[len(st) - 1 - i]:
            res = False
    if res:
        print('#{} {}'.format(t, 'Exist'))
    else:
        print('#{} {}'.format(t, 'Not exist'))