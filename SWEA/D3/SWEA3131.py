def prime_n(n):
    nums = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if nums[i] == True:
            for j in range(i + i, n, i):
                nums[j] = False
    return [i for i in range(2, n) if nums[i] == True]
print(*prime_n(10 ** 6))