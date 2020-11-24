tc = int(input())
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
print('#1')
print('1')
for i in range(2, tc + 1):
    spiral = [[0] * i for j in range(i)]
    cnt = 1
    r, c = 0, 0
    direct = 0
    print('#{}'.format(i))
    while True:
        if spiral[r][c] != 0:
            break
        spiral[r][c] = cnt
        cnt += 1
        nr = r + dy[direct]
        nc = c + dx[direct]

        if nr < 0 or nr >= len(spiral) or nc < 0 or nc >= len(spiral) or spiral[nr][nc] != 0:
            direct = (direct + 1) % 4
            nr = r + dy[direct]
            nc = c + dx[direct]
        r = nr
        c = nc
    for j in range(len(spiral)):
        for k in range(len(spiral)):
            print(spiral[j][k], end = ' ')
        print()