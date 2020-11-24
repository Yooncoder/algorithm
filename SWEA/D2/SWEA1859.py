tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    day = list(map(int, input().split()))
    val = 0
    max_val = day[n - 1]
    for i in range(n - 2 , -1, -1):
        if max_val > day[i]:
            val += max_val - day[i]
        else:
            max_val = day[i]
    print('#{} {}'.format(t, val))