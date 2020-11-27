def prime(n):
    num = [1] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if num[i] == 1:
            for j in range(i + i, n, i):
                num[j] = 0
    return [i for i in range(a, n) if num[i] == 1]


for t in range(1, int(input()) + 1):
    d, a, b = input().split()
    a = int(a)
    b = int(b)
    sol = prime(b + 1)
    cnt = 0
    for i in sol:
        if d in str(i):
            cnt += 1
        if d == '1' and str(i) == '1':
            cnt -= 1
    print('#{} {}'.format(t, cnt))