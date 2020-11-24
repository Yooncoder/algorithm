tc = int(input())
for t in range(1, tc + 1):
    data = list(map(int, input().split()))
    data.sort()
    n = len(data)
    sol = round((sum(data) - data[0] - data[-1]) / (n - 2))
    print('#{} {}'.format(t, sol))