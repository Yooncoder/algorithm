tc = int(input())

for i in range(1, tc + 1):
    n = int(input())
    nn = [[] for j in range(n)]
    mat = []
    for k in range(n):
        data = list(map(str, input().split()))
        mat.append(data)
    for l in range(3):
        new_nn = []
        idx = 0
        for z in zip(*mat):
            new_nn.append(list(reversed(z)))
            nn[idx].append(''.join(list(reversed(z))))
            idx += 1
        mat = new_nn
    print('#{}'.format(i))
    for m in nn:
        print(' '.join(m))