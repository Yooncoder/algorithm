a = int(input())

for i in range(a):
    j = list(map(int, input().split()))
    j.sort()
    print('#{0} {1}'.format(i + 1, j[9]))