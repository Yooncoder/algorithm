def solve(a, b, c, d, first):
    result = 'impossible'
    if a != 0 and d != 0 and b == 0 and c == 0:
        return result
    elif abs(first) > 1:
        return result
    elif first == -1:
        if b == 0:
            return '1' * (d + 1) + '0' * (a + 1)
        else:
            return '1' * (d + 1) + '01' * b + '0' * (a + 1)
    elif first == 1:
        if c == 0:
            return '0' * (a + 1) + '1' * (d + 1)
        else:
            return '0' * (a + 1) + '10' * c + '1' * (d + 1)
    else:
        if a == 0 and b == 0:
            return '1' * (d + 1)
        elif d == 0 and b == 0:
            return '0' * (a + 1)
        else:
            if a != 0 and d != 0:
                return '0' * (a + 1) + '10' * (b - 1) + '1' * (d + 1) + '0'
            elif a != 0 and d == 0:
                return '0' * (a + 1) + '10' * b
            elif a == 0 and d != 0:
                return '1' * (d + 1) + '01' * b
            else:
                return '01' * b + '0'


res = []
for t in range(1, int(input()) + 1):
    a, b, c, d = map(int, input().split())
    sol = solve(a, b, c, d, b - c)
    res.append(sol)
for i in range(len(res)):
    print('#{} {}'.format(i + 1, res[i]))