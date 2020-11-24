tc = 10
for t in range(1, tc + 1):
    n = int(input())
    data = list(map(int, input().split()))
    sol = 0
    for i in range(2, n - 2):
        max_d = max(data[i - 2], data[i - 1], data[i + 1], data[i + 2])
        if data[i] > max_d:
            sol += data[i] - max_d
    print('#{} {}'.format(t, sol))