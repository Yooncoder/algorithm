for t in range(1, int(input()) + 1):
    st = input()
    max_l = 0
    for i in range(len(st)):
        for j in range(len(st), i, -1):
            if i < j:
                if st[i:j] == st[i:j][::-1]:
                    max_l = max(max_l, len(st[i:j]))
                    break
    print('#{} {}'.format(t, max_l))