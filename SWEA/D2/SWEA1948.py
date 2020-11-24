tc = int(input())

for i in range(1, tc + 1):
    date = 0
    m1, d1, m2, d2 = map(int, input().split())
    for k in range(m1, m2):
        if k == 1 or k == 3 or k == 5 or k == 7 or k == 8 or k == 10 or k == 12:
            date += 31
        elif k == 2:
            date += 28
        elif k == 4 or k == 6 or k == 9 or k == 11:
            date += 30
    date = date + d2 - d1 + 1
    print('#{} {}'.format(i, date))