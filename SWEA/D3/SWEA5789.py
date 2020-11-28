for t in range(1, int(input()) + 1):
    n, q = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(q)]
    box = [0] * n
    for i in range(len(data)):
        l, r = data[i]
        for j in range(l, r + 1):
            box[j - 1] = i + 1
    print('#{}'.format(t), *box)