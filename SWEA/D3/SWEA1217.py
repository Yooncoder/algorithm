def pw(m):
    if m < 1:
        return 1
    return pw(m - 1) * n

tc = 10
for t in range(1, tc + 1):
    tt = int(input())
    n, m = map(int, input().split())
    print('#{} {}'.format(t, pw(m)))