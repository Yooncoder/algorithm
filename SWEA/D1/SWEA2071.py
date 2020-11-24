a = int(input())

for i in range(a):
    t = list(map(int, input().split()))
    j = sum(t) / len(t)
    print('#{0} {1}'.format(i + 1, round(j)))