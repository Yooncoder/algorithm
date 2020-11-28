res = []
for i in range(1, int(input()) + 1):
    d, a, b, f = map(int, input().split())
    t = d / (a + b)
    sol = t * f
    res.append(sol)
for i in range(len(res)):
    print('#{} {}'.format(i + 1, res[i]))