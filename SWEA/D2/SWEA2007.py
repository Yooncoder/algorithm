tc = int(input())
for t in range(1, tc + 1):
    l = input()
    sol = False
    i = 1
    while True:
        if l[ : i] == l[i : i * 2]:
            sol = True
            break
        else:
            i += 1
    if sol:
        print('#{} {}'.format(t, i))