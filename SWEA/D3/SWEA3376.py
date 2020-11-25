for t in range(1, int(input()) + 1):
    n = int(input())
    table = {i : 0 for i in range(n + 1)}
    table[1], table[2], table[3], table[4] = 1, 1, 1, 2
    for i in range(5, n + 1):
        table[i] = table[i - 1] + table[i - 5]
    print('#{} {}'.format(t, table[n]))