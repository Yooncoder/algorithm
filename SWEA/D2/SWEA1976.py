tc = int(input())
for t in range(1, tc + 1):
    h1, m1, h2, m2 = map(int, input().split())
    hour = h1 + h2
    minute = m1 + m2
    if minute > 59:
        hour += 1
        minute -= 60
    if hour > 12:
        hour -= 12

    print('#{} {} {}'.format(t, hour, minute))