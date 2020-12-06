for t in range(1, int(input()) + 1):
    n, a, b = map(int, input().split())
    max_val = min(a, b)
    if n <= a + b:
        min_val = a + b - n
    else:
        min_val = 0
    print('#{} {} {}'.format(t, max_val, min_val))