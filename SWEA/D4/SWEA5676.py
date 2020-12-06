def ccw(a, b, c):
    op = (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])
    if op > 0:
        return 1
    elif op:
        return -1
    else:
        return 0


def intersection(x, y):
    a, b = x[0], x[1]
    c, d = y[0], y[1]
    if ccw(a, b, c) == 0 and ccw(a, b, d) == 0:
        if sum(a) > sum(b):
            a, b = b, a
        if sum(c) > sum(d):
            c, d = d, c
        if (sum(b) < sum(c)) or (sum(d) < sum(a)):
            return 0
        elif (sum(b) == sum(c)) or (sum(d) == sum(a)):
            return 1
        else:
            return -1
    if (ccw(a, b, c) == ccw(a, b, d)) or (ccw(c, d, a) == ccw(c, d, b)):
        return 0
    else:
        return 1


for t in range(1, int(input()) + 1):
    x1, y1, x2, y2 = map(int, input().split())
    line = list(map(int, input().split()))
    lines = [[(x1, y1), (x2, y1)], [(x2, y1), (x2, y2)], [(x1, y2), (x2, y2)], [(x1, y1), (x1, y2)]]
    points = [[x1, y1], [x1, y2], [x2, y1], [x2, y2]]
    sol = 0
    for i in range(4):
        s = intersection(((line[0], line[1]), (line[2], line[3])), (lines[i][0], lines[i][1]))
        if s == -1:
            sol = 4
            break
        sol += s
        s = intersection(((line[0], line[1]), (line[2], line[3])), (points[i], points[i]))
        if s:
            sol -= 1
    print('#{} {}'.format(t, sol))