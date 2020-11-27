for t in range(1, int(input()) + 1):
    clap = list(map(int, input()))
    cnt = 0
    clapping = clap[0]
    for i in range(1, len(clap)):
        if clapping < i and clap[i] != 0:
            cnt += i - clapping
            clapping = i + clap[i]
        else:
            clapping += clap[i]
    print('#{} {}'.format(t, cnt))