tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    max_sum = 0
    sol = 0
    for i in range(n):
        sol = 0
        sol += nums[i]
        if max_sum < sol:
            max_sum = sol
        for j in range(i + 1, n):
            if sol > 0 and nums[j] + sol > 0:
                sol += nums[j]
            else:
                break
            if max_sum < sol:
                max_sum = sol
    print('#{} {}'.format(t, max_sum))