tc = 10
for t in range(1, tc + 1):
    n = int(input())
    password = list(map(int, input().split()))
    order = int(input())
    orders = list(map(str, input().split()))
    order_lst = [[] for _ in range(order)]
    for i in range(order):
        orders.remove('I')
    orders.reverse()
    for i in range(len(orders)):
        orders[i] = int(orders[i])
    for i in range(order):
        for j in range(orders[-2] + 2):
            order_lst[i].append(orders.pop())
    for i in range(order):
        for j in range(order_lst[i][1]):
            password.insert(order_lst[i][0] + j, order_lst[i][j + 2])
    print('#{} '.format(t), end = '')
    print(*password[0 : 10])