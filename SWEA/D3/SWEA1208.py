tc = 10
 
for t in range(1, tc + 1):
    n = int(input())
    data = list(map(int, input().split()))
    data.sort()
    for i in range(n):
        data[0] += 1
        data[-1] -= 1
        data.sort()
    print('#{} {}'.format(t, data[-1] - data[0]))