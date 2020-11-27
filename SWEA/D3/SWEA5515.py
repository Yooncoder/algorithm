date = [0] * 12
date[0] = 4
for i in range(1, 12):
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
        date[i] += date[i - 1] + 31
    elif i == 2:
        date[i] += date[i - 1] + 29
    else:
        date[i] += date[i - 1] + 30

for t in range(1, int(input()) + 1):
    m, d = map(int, input().split())
    sol = (date[m - 1] + d - 1) % 7

    print('#{} {}'.format(t, sol))