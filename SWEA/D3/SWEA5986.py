def primes(n):
    nums = [1] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if nums[i] == 1:
            for j in range(i + i, n, i):
                nums[j] = 0
    return [i for i in range(2, n) if nums[i] == 1]


for t in range(1, int(input()) + 1):
    n = int(input())
    sol = primes(n)
    cnt = 0
    l = len(sol)
    for i in range(l):
        for j in range(i, l):
            for k in range(j, l):
                if sol[i] + sol[j] + sol[k] == n:
                    cnt += 1
    print('#{} {}'.format(t, cnt))