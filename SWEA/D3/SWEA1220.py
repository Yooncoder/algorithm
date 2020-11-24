def remover(list):
    my_set = [0]
    result = []
    for i in list:
        if i not in my_set:
            result.append(i)
    return result

tc = 10

for i in range(1, tc + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    s_cnt = 0
    for j in range(100):
        mag = remover(list(zip(*board))[j])
        for k in range(len(mag)):
            if mag[0] == 2:
                del mag[0]
            if mag[len(mag) - 1] == 1:
                del mag[len(mag) - 1]
        cnt = 0
        for k in range(len(mag) - 1):
            if mag[k] == 1 and mag[k + 1] == 2:
                cnt += 1
        s_cnt += cnt
    print('#{} {}'.format(i , s_cnt))