for t in range(1, int(input()) + 1):
    a, b, c = map(int, input().split())
    min_v = min(a, b)
    print('#{} {}'.format(t, c // min_v))