for t in range(1, int(input()) + 1):
    d, h, m = map(int, input().split())
    dd = d - 11
    if dd == 0:
        if h >= 11:
            if m < 11:
                print('#{} {}'.format(t, -1))
            else:
                hh = h - 11
                print('#{} {}'.format(t, hh * 60 + m - 11))
        else:
            print('#{} {}'.format(t, -1))
    else:
        hh = h - 11
        mm = m - 11
        print('#{} {}'.format(t, dd * 1440 + hh * 60 + mm))