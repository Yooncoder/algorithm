tc = int(input())
for i in range(1, tc + 1):
    money = int(input())
    won = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    sol = []
    print('#{}'.format(i))
    for j in won:
        a, b = divmod(money, j)
        money = b
        sol.append(a)
    for k in range(len(sol)):
        print('{} '.format(sol[k]), end = '')
    print()