tc = int(input())

for i in range(1, tc + 1):
    sudoku = []
    row = []
    col = []
    print('#{} '.format(i), end = '')
    sum_row = []
    sum_col = []
    cnt = 0
    for j in range(9):
        row.append(list(map(int, input().split())))
    for k in range(9):
        col = []
        for l in range(9):
            col.append(row[l][k])
        sum_row.append(sum(row[k]))
        # print(row[k])
        sum_col.append(sum(col))
    sum_dia = []
    for j in range(0, 7, 3):
        for k in range(0, 7, 3):
            sudoku = []
            for x in range(3):
                for y in range(3):
                    sudoku.append(row[j + x][k + y])
            sum_dia.append(sum(sudoku))

    for k in range(9):
        if sum_row[k] != 45 or sum_col[k] != 45 or sum_dia[k] != 45:
            cnt += 1
    if cnt > 0:
        print(0)
    else:
        print(1)