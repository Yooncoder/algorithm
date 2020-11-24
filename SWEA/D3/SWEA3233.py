tc = int(input())
for t in range(1, tc + 1):
    a, b = map(int, input().split())
    sol = int(a * a / b / b)
    print('#{} {}'.format(t, sol))