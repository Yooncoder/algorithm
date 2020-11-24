tc = int(input())
for t in range(1, tc + 1):
    n, a, b = list(map(int, input().split()))
    num = 0
    nums = []
    while True:
        num += 1
        if num * num >= n:
            if num * num != n:
                num -= 1
            break
    nums.append([num, num])
    r = num + 1
    while True:
        r -= 1
        c = n // r
        nums.append([r, c])
        if n % r == 0:
            break
    sol = 99999999
    for i in nums:
        k = a * (abs(i[0] - i[1])) + b * (n - (i[0] * i[1]))
        if sol > k:
            sol = k
    print('#{} {}'.format(t, sol))