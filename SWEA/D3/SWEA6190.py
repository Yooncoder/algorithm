def check(ex):
    a = ex % 10
    ex = int(ex / 10)
    while ex != 0:
        if ex % 10 > a:
            return False
        a = ex % 10
        ex = int(ex / 10)
    return True


for t in range(1, int(input()) + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    data = []
    sol = -1
    for i in range(n):
        for j in range(i + 1, n):
            ex = nums[i] * nums[j]
            if sol < ex:
                if check(ex):
                    sol = ex
    print('#{} {}'.format(t, sol))