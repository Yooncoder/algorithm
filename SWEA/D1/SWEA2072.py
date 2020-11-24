a = int(input())

for i in range(a):
    t = list(map(int, input().split()))
    odd_sum = 0
    for j in range(len(t)):
        if t[j] % 2 == 1:
            odd_sum += t[j]
    print('#{0} {1}'.format(i + 1, odd_sum))