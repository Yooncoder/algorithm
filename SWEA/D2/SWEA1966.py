tc = int(input())

for i in range(1, tc + 1):
    n = int(input())
    data = list(map(int, input().split()))
    data.sort()
    print('#{} '.format(i), end = '')
    for j in range(n):
        print(data[j], end = ' ')
    print()