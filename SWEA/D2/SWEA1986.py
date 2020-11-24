tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    sol = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            sol += i
        else:
            sol -= i
    print('#{} {}'.format(t, sol))