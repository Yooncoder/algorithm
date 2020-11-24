tc = 10
for t in range(1, tc + 1):
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(100)]
    sums = []
    dia = []
    dia2 = []

    dia_sums = []
    for i in mat:
        sums.append(sum(i))
    for i in range(100):
        col = []
        for j in range(100):
            col.append(mat[j][i])
        sums.append(sum(col))
    for i in range(100):
        dia.append(mat[i][i])
        dia2.append(mat[i][99 - i])
    sums.append(sum(dia))
    sums.append(sum(dia2))

    print('#{} {}'.format(t, max(sums)))