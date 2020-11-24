tc = int(input())

for i in range(1, tc + 1):
    case = int(input())
    distance = 0
    speed = 0
    for j in range(case):
        cnt = list(map(int, input().split()))
        if cnt[0] == 0:
            speed = speed
        elif cnt[0] == 1:
            speed += cnt[1]
        elif cnt[0] == 2:
            speed -= cnt[1]
        if speed < 0:
            speed = 0
        distance += speed
    print('#{} {}'.format(i, distance))