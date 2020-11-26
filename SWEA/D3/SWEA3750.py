sols = []
for t in range(1, int(input()) + 1):
    n = int(input())

    while 1:
        n = str(n)
        if len(n) == 1:
            sols.append(n)
            break
        else:
            new = []
            for i in n:
                new.append(int(i))
            n = sum(new)
j = 0
for i in sols:
    j += 1
    print('#{} {}'.format(j, i))