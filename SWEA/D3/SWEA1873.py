tc = int(input())
for t in range(1, 1 + tc):
    h, w = map(int, input().split())
    field = [list(map(str, input())) for _ in range(h)]
    n = int(input())
    tank = input()
    for r in range(h):
        for c in range(w):
            if field[r][c] == '<' or field[r][c] == '>' or field[r][c] == '^' or field[r][c] == 'v':
                x, y = r, c
                break
    i = 0
    while i < n:
        if tank[i] == 'S':
            if field[x][y] == '<':
                for j in range(y - 1, -1, -1):
                    if field[x][j] == '*':
                        field[x][j] = '.'
                        break
                    if field[x][j] == '#':
                        break
            if field[x][y] == '>':
                for j in range(y + 1, w):
                    if field[x][j] == '*':
                        field[x][j] = '.'
                        break
                    if field[x][j] == '#':
                        break
            if field[x][y] == '^':
                for j in range(x - 1, -1, -1):
                    if field[j][y] == '*':
                        field[j][y] = '.'
                        break
                    if field[j][y] == '#':
                        break
            if field[x][y] == 'v':
                for j in range(x + 1, h):
                    if field[j][y] == '*':
                        field[j][y] = '.'
                        break
                    if field[j][y] == '#':
                        break
        if tank[i] == 'U':
            if x - 1 < 0 or x - 1 > h - 1 or y < 0 or y > w - 1:
                field[x][y] = '^'
                i += 1
                continue
            else:
                if field[x - 1][y] != '.':
                    field[x][y] = '^'
                elif field[x - 1][y] == '.':
                    field[x][y], field[x - 1][y] = '.', '^'
                    x, y = x - 1, y
        if tank[i] == 'D':
            if x + 1 < 0 or x + 1 > h - 1 or y < 0 or y > w - 1:
                field[x][y] = 'v'
                i += 1
                continue
            else:
                if field[x + 1][y] != '.':
                    field[x][y] = 'v'
                elif field[x + 1][y] == '.':
                    field[x][y], field[x + 1][y] = '.', 'v'
                    x, y = x + 1, y
        if tank[i] == 'L':
            if x < 0 or x > h - 1 or y - 1 < 0 or y - 1 > w - 1:
                field[x][y] = '<'
                i += 1
                continue
            else:
                if field[x][y - 1] != '.':
                    field[x][y] = '<'
                elif field[x][y - 1] == '.':
                    field[x][y], field[x][y - 1] = '.', '<'
                    x, y = x, y - 1
        if tank[i] == 'R':
            if x < 0 or x > h - 1 or y + 1 < 0  or y + 1 > w - 1:
                field[x][y] = '>'
                i += 1
                continue
            else:
                if field[x][y + 1] != '.':
                    field[x][y] = '>'
                elif field[x][y + 1] == '.':
                    field[x][y], field[x][y + 1] = '.', '>'
                    x, y = x, y + 1
        i += 1
    print('#{} {}'.format(t, ''.join(map(str, field[0]))))
    for i in range(1, h):
        print('{}'.format(''.join(map(str, field[i]))))