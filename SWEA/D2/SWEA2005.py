tc = int(input())

for i in range(1, tc + 1):
    n = int(input())
    print('#{}'.format(i))
    for j in range(n):
        line = []
        for k in range(j + 1):
            if k == 0 or k == j:
                line.append(1)
            elif j > 1:
                line.append(lines[k - 1] + lines[k])
        lines = list(line)
        print(' '.join(map(str, line)))