tc = 10
for t in range(1, tc + 1):
    n = int(input())
    m = input()
    litter = input()
    cnt = 0
    for i in range(len(litter) - len(m) + 1):
        if m in litter[i : i + len(m)]:
            cnt += 1
    print('#{} {}'.format(t, cnt))