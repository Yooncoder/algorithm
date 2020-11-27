for t in range(1, int(input()) + 1):
    data = [list(map(str, input())) for _ in range(5)]
    st = ''
    max_len = max(map(len, data))
    for i in range(max_len):
        for j in data:
            if len(j) <= i:
                continue
            st += j[i]
    print('#{} {}'.format(t, st))