tc = int(input())
for t in range(1, tc + 1):
    l = input()
    mid = len(l) // 2
    cnt = 0
    for i in range(mid):
        if l[i] == l[len(l) - 1 - i]:
            cnt += 1
    if cnt == mid:
        print('#{} {}'.format(t, 1))
    else:
        print('#{} {}'.format(t, 0))