for t in range(1, int(input()) + 1):
    k = int(input())
    mag = [list(map(int, input().split())) for _ in range(4)]

    for i in range(k):
        idx, dir = map(int, input().split())
        idx -= 1
        rotation = [(idx, dir)]

        left = dir
        for j in range(idx - 1, -1, -1):
            if mag[j][2] != mag[j + 1][6]:
                left *= -1
                rotation.append((j, left))
            else:
                break

        right = dir
        for j in range(idx + 1, 4):
            if mag[j][6] != mag[j - 1][2]:
                right *= -1
                rotation.append((j, right))
            else:
                break

        for idx, dir in rotation:
            if dir == 1:
                mag[idx] = [mag[idx].pop()] + mag[idx]
            else:
                x = mag[idx].pop(0)
                mag[idx].append(x)

    sol = 0
    for i in range(4):
        sol += mag[i][0] * 2 ** i

    print('#{} {}'.format(t, sol))