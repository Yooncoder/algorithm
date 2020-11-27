def hamberger(idx, s, k):
    global max_s
    if idx == n:
        max_s = max(max_s, s)
        return
    else:
        for i in range(2):
            if i == 0:
                hamberger(idx + 1, s, k)
            else:
                if k + data[idx][1] > l:
                    return
                else:
                    hamberger(idx + 1, s + data[idx][0], k + data[idx][1])


for t in range(1, int(input()) + 1):
    n, l = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    max_s = 0

    hamberger(0, 0, 0)
    print('#{} {}'.format(t, max_s))