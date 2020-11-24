pw_code = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

tc = int(input())
for t in range(1, tc + 1):
    n, m = map(int, input().split())
    code = [input() for _ in range(n)]
    point = []
    for i in range(n):
        for j in range(m - 1, -1, -1):
            if code[i][j] == '1':
                point.append((i, j))
                break
    h = len(point)
    pw = []
    num = ''
    sol = 0
    for i in range(point[0][1] - 55, point[0][1], 7):
        pw.append(code[point[0][0]][i : i + 7])
    for i in pw:
        if i in pw_code:
            num += str(pw_code.index(i))
    for i in range(len(num)):
        if i % 2 == 0:
            sol += int(num[i]) * 3
        else:
            sol += int(num[i])
    res = 0
    if sol % 10 == 0:
        for i in range(len(num)):
            res += int(num[i])
        print('#{} {}'.format(t, res))
    else:
        print('#{} {}'.format(t, 0))