def sums(sol, idx, k, arr):
    if k == 3:
        sols.append(sol)
        return
    for i in range(idx, 7):
        if check[i] == 1:
            continue
        check[i] = 1
        sums(sol + arr[i], idx + 1, k + 1, arr)
        check[i] = 0


for t in range(1, int(input()) + 1):
    data = list(map(int, input().split()))
    sols = []
    check = [0] * 8
    sums(0, 0, 0, data)
    sols = list(set(sols))
    sols.sort(reverse=True)
    print('#{} {}'.format(t, sols[4]))