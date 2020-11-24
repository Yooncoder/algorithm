tc = 10
for t in range(1, tc + 1):
    n = int(input())
    password = list(map(str, input().split()))
    m = int(input())
    od = list(map(str, input().split()))
    i_cnt = od.count('I')
    d_cnt = od.count('D')
    i_lst = [[] for _ in range(i_cnt)]
    d_lst = [[] for _ in range(d_cnt)]

    for i in range(len(od)):
        if od[i] == 'I':
            for j in range(int(od[i + 2])):
                password.insert(int(od[i + 1]) + j, od[j + i + 3])
        if od[i] == 'D':
            del password[int(od[i + 1]) : int(od[i + 1]) + int(od[i + 2])]
    print('#{} '.format(t), end = '')
    print(*password[0 : 10])