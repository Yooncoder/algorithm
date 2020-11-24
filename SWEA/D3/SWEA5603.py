tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    heys = []
    cnt = 0
    for i in range(n):
        heys.append(int(input()))
    heys_avr = sum(heys) // len(heys)
    for i in heys:
        if i < heys_avr:
            cnt += heys_avr - i
    print('#{} {}'.format(t, cnt))