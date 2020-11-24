tc = int(input())
for t in range(1, tc + 1):
    data = str(input())
    case = '0' * len(data)
    data = list(map(str, data))
    case = list(map(str, case))
    res = True
    cnt = 0
    while res:
        for i in range(len(data)):
            if data[i] != case[i]:
                if data[i] == '1':
                    for j in range(i, len(data)):
                        case[j] = '1'
                    cnt += 1
                else:
                    for j in range(i, len(data)):
                        case[j] = '0'
                    cnt += 1
        if case == data:
            res = False
    print('#{} {}'.format(t, cnt))