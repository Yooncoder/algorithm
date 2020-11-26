for t in range(1, int(input()) + 1):
    n = int(input())
    nums = []
    while len(nums) != n:
        nums += list(map(int, input().split()))

    number = ''.join(map(str, nums))
    res = -1
    for i in range(10):
        if not i in nums:
            num = res = i
            break
    if res == -1:
        num = 10
        while res == -1:
            if number.find(str(num)) == -1:
                break
            num += 1
    print('#{} {}'.format(t, num))